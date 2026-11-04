import re
from datetime import datetime

import itertools    #for optimization framework

def convert_to_24h(time_str: str) -> str:
    parsed_time = datetime.strptime(time_str, "%I:%M%p")
    return parsed_time.strftime("%H:%M")

def contains_day(substr):
    target_str=substr.lower()
    if "monday" in target_str:
        return True
    if "tuesday" in target_str:
        return True
    if "wednesday" in target_str:
        return True
    if "thursday" in target_str:
        return True
    if "friday" in target_str:
        return True
    if "saturday" in target_str:
        return True
    if "sunday" in target_str:
        return True

    return False

def strip_list(list_arg):
    for idx in range(0, len(list_arg)):
        list_arg[idx] = list_arg[idx].strip()

def time_to_minutes(time_str: str) -> int:
    #Converts 24 hour format to minutes from midnight.
    nums = time_str.split(':')
    hours = int(nums[0])
    minutes = int(nums[1])
    return hours*60 + minutes

def print_schedule(analyzed_schedule):
    """
    Prints a clear summary of an optimized schedule layout.
    Expects a dictionary item from our optimizer's analyzed results.
    """
    print("=" * 50)
    print(f"🗓️  SCHEDULE OVERVIEW  "
          f"({analyzed_schedule['num_days']} Days | {analyzed_schedule['total_span_hours']:.2f} Hours)")
    print("=" * 50)
    
    # Extract the tuple of section objects
    sections = analyzed_schedule["sections"]
    
    for idx, section in enumerate(sections, start=1):
        # Safely get the title we added in Step 1 (or fallback if missing)
        class_title = getattr(section, 'parent_title', f"Course #{idx}")
        
        print(f"📚 {class_title}:")
        
        # Loop through the times inside this section's schedule
        for meet in section.Schedule:
            # Format the day list into a nice string (e.g. ['M', 'W'] -> M, W)
            days_str = ", ".join(meet.Days)
            start_time = meet.Time[0]
            end_time = meet.Time[1]
            
            print(f"   ↳ Days: [{days_str}]  |  Time: {start_time} - {end_time}")
    print("=" * 50 + "\n")

class ClassGenus:
    def __init__(self, name):
        self.ClassTitle=name
        self.Sections=[]
    def PushSection(self, mysection):
        mysection.parent_title = self.ClassTitle
        self.Sections.append(mysection)
    def Print(self):
        print(f"Title of Class Genus: {self.ClassTitle}")
        for idx,section in enumerate(self.Sections, start=1):
            print(f"Section {idx}:", end="")
            section.Print()

class Section:
    def __init__(self):
        self.Schedule=[]
        self.parent_title = ""
    def PushDayTime(self, mydaytime):
        self.Schedule.append(mydaytime)
    def Print(self):
        for meet in self.Schedule:
            meet.Print()

class MyDayTime:
    def __init__(self):
        self.Days=[]
        self.Time=[]
    def SetDays(self, days_list):
        self.Days=days_list[:]
    def SetTime(self, time_list):
        self.Time=time_list[:]
    def get_minutes(self):
        #Returns (start_min, end_min)
        return time_to_minutes(self.Time[0]), time_to_minutes(self.Time[1])
    def Print(self):
        print(self.Days)
        print(self.Time)

#begin Optimization framework


class ScheduleOptimizer:
    def __init__(self, all_classes, total_required, must_include_titles):
        """
        all_classes: List of ClassGenus objects
        total_required: Total number of classes to take (int)
        must_include_titles: List of strings matching ClassTitle
        """
        self.all_classes = all_classes
        self.total_required = total_required
        self.must_include_titles = set(must_include_titles)
        
    def _is_time_conflict(self, section1, section2) -> bool:
        """Returns True if two sections overlap on any day."""
        for meet1 in section1.Schedule:
            for meet2 in section2.Schedule:
                # Check if they share any days
                shared_days = set(meet1.Days) & set(meet2.Days)
                if shared_days:
                    start1, end1 = meet1.get_minutes()
                    start2, end2 = meet2.get_minutes()
                    # Standard overlap condition
                    if max(start1, start2) < min(end1, end2):
                        return True
        return False

    def _get_valid_class_combinations(self):
        """Filters class combinations matching your required selection constraints."""
        must_classes = [c for c in self.all_classes if c.ClassTitle in self.must_include_titles]
        optional_classes = [c for c in self.all_classes if c.ClassTitle not in self.must_include_titles]
        
        needed_optional = self.total_required - len(must_classes)
        
        valid_combinations = []
        # Generate combinations of the remaining optional classes
        for opt_combo in itertools.combinations(optional_classes, needed_optional):
            valid_combinations.append(must_classes + list(opt_combo))
            
        return valid_combinations

    def generate_schedules(self):
        """Generates all non-overlapping schedule variations."""
        possible_schedules = []
        class_combos = self._get_valid_class_combinations()
        
        for class_list in class_combos:
            # Extract lists of sections for the selected classes
            # e.g., [[sec1, sec2], [secA, secB]]
            sections_pool = [c.Sections for c in class_list]
            
            # Generate Cartesian product of all section combinations
            for section_combo in itertools.product(*sections_pool):
                if not self._has_internal_conflict(section_combo):
                    possible_schedules.append(section_combo)
                    
        return possible_schedules

    def _has_internal_conflict(self, section_combo) -> bool:
        """Checks if a concrete layout of sections has any collisions."""
        for sec1, sec2 in itertools.combinations(section_combo, 2):
            if self._is_time_conflict(sec1, sec2):
                return True
        return False

    # --- SCORE & ANALYZE METRICS ---
    def analyze_schedule(self, section_combo):
        """Calculates specific constraints for ranking."""
        days_active = set()
        day_bounds = {} # day: [min_start, max_end]
        
        for section in section_combo:
            for meet in section.Schedule:
                start_m, end_m = meet.get_minutes()
                for day in meet.Days:
                    days_active.add(day)
                    if day not in day_bounds:
                        day_bounds[day] = [start_m, end_m]
                    else:
                        day_bounds[day][0] = min(day_bounds[day][0], start_m)
                        day_bounds[day][1] = max(day_bounds[day][1], end_m)
                        
        # Total span across all days (sum of end - start)
        total_span_minutes = sum((bounds[1] - bounds[0]) for bounds in day_bounds.values())
        
        return {
            "num_days": len(days_active),
            "total_span_hours": total_span_minutes / 60.0,
            "sections": section_combo
        }


#end Optimization Framework



with open("availability.txt") as file_object:
    raw_text=file_object.readlines()

all_classes=[]

section = Section()

class_name=""
meeting_days=[]
meeting_window=[]
day_time={'Days' : [], 'Time' : []}

found_time=False           #Just found the day, time follows immediately
begin_class=False          #Looking for sections
begin_class_instance=False #Looking for day/times
section_empty=True
n = len(raw_text)
for i, line in enumerate(raw_text, 1):
    if (line == '\n' or len(line.strip()) == 0) and i != n:
        continue
    if i == n:
        if begin_class_instance:
            classGenus.PushSection(section)
            print(f"Pushing last section for {class_name}")
        classGenus.Print()
        all_classes.append(classGenus)
        break
    if (line.strip())[0]=='[':
        if begin_class_instance:
            classGenus.PushSection(section)
        if begin_class:
            classGenus.Print()
            all_classes.append(classGenus)
        print(f"Found new class genus: {line}")
        result=re.findall(r'\[(.*?)\]', line)
        class_name=result[0]
        classGenus = ClassGenus(class_name)
        begin_class=True
        begin_class_instance = False
    if found_time:
#        print(line, end='')
        meeting_window=line.split(' ')
#        print(f"Meeting window: {meeting_window}")
        first=convert_to_24h(meeting_window[0])
        second=convert_to_24h(meeting_window[2].strip())
        temp_time = [first, second]
        print(f"I.e.: {first} - {second}")
#        print(f"Printing day-time: {day_time}")
        
        temp_dayTime = MyDayTime()
        temp_dayTime.SetDays(meeting_days[:])
        temp_dayTime.SetTime(temp_time[:])
        print(f"Printing temp day time:", end='')
        temp_dayTime.Print()

        section.PushDayTime(temp_dayTime)
        section_empty=False

        meeting_days.clear()
        meeting_window.clear()
        temp_time.clear()
        found_time=False
    if contains_day(line) and begin_class_instance:
        print(line, end='')
        meeting_days=line.split(' ')
        strip_list(meeting_days)
#        print(f"Meeting days: {meeting_days}")
        found_time=True
    if "section" in line.lower() and begin_class:
        if begin_class_instance:
            print("Have begun second or greater instance")
            print("Printing schedule of section")
            section.Print()
            if not section_empty:
                classGenus.PushSection(section)
        begin_class_instance=True
        section = Section()
        section_empty=True

#        print(f"Starting new class instance")

print("\n\nOk, we're done organizing the data.")
for genus in all_classes:
    genus.Print()



# Now, we need to optimize and make parameters possible

optimizer = ScheduleOptimizer(
    all_classes=all_classes,
    total_required=5,
    must_include_titles=["CPSC 481", "MATH 340", "MATH 335", "PHYS 227"]
)

# 1. Gather all legal layout options
valid_options = optimizer.generate_schedules()

# 2. Extract metrics for each one
analyzed_schedules = [optimizer.analyze_schedule(sched) for sched in valid_options]

# 3. Sort by your preference constraints!
# Example: Sort primarily by FEWEST days on campus, then by SHORTEST time spent on campus

best_schedules = sorted(
    analyzed_schedules, 
    key=lambda x: (x["num_days"], x["total_span_hours"])
)

"""
best_schedules = sorted(
    analyzed_schedules, 
    key=lambda x: (x["total_span_hours"], x["num_days"])
)
"""

# Print your winning setup
if best_schedules:
    winner = best_schedules[0]
    print(f"🥇 BEST SCHEDULE FOUND:")
    print(f"Days on campus: {winner['num_days']}")
    print(f"Total Weekly Campus Window: {winner['total_span_hours']:.2f} hours")
else:
    print("No valid, conflict-free schedule combination fits your criteria.")

for rank, schedule in enumerate(best_schedules[:10], start=1):
    print(f"RANK #{rank}")
    print_schedule(schedule)




