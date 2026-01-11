"""
Exercise 2: Interval Scheduling Problems
Greedy algorithms for interval scheduling, partitioning, and lateness
"""


def interval_scheduling(intervals):
    """
    Interval Scheduling: Select maximum number of non-overlapping intervals
    
    Greedy strategy: Always choose the interval that ends earliest
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n)
    
    Args:
        intervals: List of tuples (start, end)
    
    Returns:
        List of selected intervals
    """
    # Sort by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    selected = []
    last_end = -1
    
    for start, end in sorted_intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected


def interval_partitioning(intervals):
    """
    Interval Partitioning: Find minimum number of resources needed
    
    Greedy strategy: Assign each interval to any compatible resource,
    or create a new resource if none is compatible
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Returns:
        List of lists, where each inner list contains intervals for one resource
    """
    # Sort by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    resources = []  # Each resource is a list of intervals
    
    for start, end in sorted_intervals:
        # Try to assign to existing resource
        assigned = False
        for resource in resources:
            # Check if compatible (no overlap with last interval in resource)
            if resource and resource[-1][1] <= start:
                resource.append((start, end))
                assigned = True
                break
        
        # If no compatible resource, create new one
        if not assigned:
            resources.append([(start, end)])
    
    return resources


def minimize_lateness(jobs):
    """
    Scheduling to Minimize Lateness
    
    Greedy strategy: Schedule jobs in order of increasing deadline
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        jobs: List of tuples (processing_time, deadline)
    
    Returns:
        Tuple (schedule, max_lateness)
        schedule: List of job indices in order
        max_lateness: Maximum lateness
    """
    # Sort by deadline
    indexed_jobs = [(i, pt, dl) for i, (pt, dl) in enumerate(jobs)]
    sorted_jobs = sorted(indexed_jobs, key=lambda x: x[2])
    
    schedule = []
    current_time = 0
    max_lateness = 0
    
    for job_idx, processing_time, deadline in sorted_jobs:
        schedule.append(job_idx)
        current_time += processing_time
        lateness = max(0, current_time - deadline)
        max_lateness = max(max_lateness, lateness)
    
    return schedule, max_lateness


def demonstrate_interval_problems():
    """Demonstrate interval scheduling problems"""
    print("=" * 70)
    print("Interval Scheduling Problems")
    print("=" * 70)
    
    # Example 1: Interval Scheduling
    print("\n1. Interval Scheduling (Maximum Non-Overlapping Intervals)")
    print("-" * 70)
    
    intervals1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    
    print("Intervals:", intervals1)
    selected = interval_scheduling(intervals1)
    print(f"\nSelected intervals (greedy): {selected}")
    print(f"Maximum number of non-overlapping intervals: {len(selected)}")
    
    # Example 2: Interval Partitioning
    print("\n\n2. Interval Partitioning (Minimum Resources)")
    print("-" * 70)
    
    intervals2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
    
    print("Intervals:", intervals2)
    resources = interval_partitioning(intervals2)
    print(f"\nPartitioning into {len(resources)} resources:")
    for i, resource in enumerate(resources, 1):
        print(f"  Resource {i}: {resource}")
    
    # Example 3: Minimize Lateness
    print("\n\n3. Minimize Maximum Lateness")
    print("-" * 70)
    
    jobs = [
        (3, 6),   # Job 0: 3 units, deadline 6
        (2, 8),   # Job 1: 2 units, deadline 8
        (1, 9),   # Job 2: 1 unit, deadline 9
        (4, 9),   # Job 3: 4 units, deadline 9
        (3, 14),  # Job 4: 3 units, deadline 14
        (2, 15),  # Job 5: 2 units, deadline 15
    ]
    
    print("Jobs (processing_time, deadline):")
    for i, (pt, dl) in enumerate(jobs):
        print(f"  Job {i}: {pt} units, deadline {dl}")
    
    schedule, max_lateness = minimize_lateness(jobs)
    print(f"\nOptimal schedule (by deadline): {schedule}")
    print(f"Maximum lateness: {max_lateness}")
    
    # Show timeline
    print("\nTimeline:")
    current_time = 0
    for job_idx in schedule:
        pt, dl = jobs[job_idx]
        finish_time = current_time + pt
        lateness = max(0, finish_time - dl)
        print(f"  Job {job_idx}: [{current_time} - {finish_time}], deadline {dl}, lateness {lateness}")
        current_time = finish_time
    
    # Example 4: Classroom scheduling
    print("\n\n4. Classroom Scheduling Application")
    print("-" * 70)
    
    classes = [
        ("Math", 9, 10),
        ("Physics", 9, 11),
        ("Chemistry", 10, 12),
        ("Biology", 11, 13),
        ("History", 12, 13),
        ("English", 13, 14),
    ]
    
    intervals = [(start, end) for _, start, end in classes]
    resources = interval_partitioning(intervals)
    
    print(f"Classes need {len(resources)} classrooms:")
    for i, resource in enumerate(resources, 1):
        print(f"  Classroom {i}:")
        for interval in resource:
            class_name = next(name for name, s, e in classes if (s, e) == interval)
            print(f"    {class_name} ({interval[0]}:00 - {interval[1]}:00)")
    
    print("\n" + "=" * 70)
    print("Key Greedy Strategies:")
    print("=" * 70)
    print("1. Interval Scheduling: Choose earliest finishing time")
    print("2. Interval Partitioning: Assign to any compatible resource")
    print("3. Minimize Lateness: Schedule by earliest deadline first")
    print("4. All use O(n log n) time for sorting")


if __name__ == "__main__":
    demonstrate_interval_problems()
