"""
Exercise 3: Applications of Stable Matching
Demonstrates real-world applications of the stable matching problem
"""


def gale_shapley(men_preferences, women_preferences):
    """Gale-Shapley algorithm (from exercise 1)"""
    free_men = list(men_preferences.keys())
    engaged = {}
    proposals = {man: 0 for man in free_men}
    
    women_rankings = {}
    for woman, prefs in women_preferences.items():
        women_rankings[woman] = {man: rank for rank, man in enumerate(prefs)}
    
    while free_men:
        man = free_men[0]
        
        if proposals[man] >= len(men_preferences[man]):
            free_men.pop(0)
            continue
        
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1
        
        if woman not in engaged:
            engaged[woman] = man
            free_men.pop(0)
        else:
            current_man = engaged[woman]
            if women_rankings[woman][man] < women_rankings[woman][current_man]:
                engaged[woman] = man
                free_men.pop(0)
                free_men.append(current_man)
    
    return engaged


def hospital_resident_matching(residents, hospitals, hospital_capacities):
    """
    Hospital-Resident Matching Problem (many-to-one matching).
    
    This is a generalization of stable matching where:
    - Each hospital can accept multiple residents
    - Each resident can only go to one hospital
    
    Args:
        residents: Dict mapping resident -> list of hospitals (preferences)
        hospitals: Dict mapping hospital -> list of residents (preferences)
        hospital_capacities: Dict mapping hospital -> capacity (int)
    
    Returns:
        Dict mapping hospital -> list of residents
    """
    # Initialize
    free_residents = list(residents.keys())
    assignments = {hospital: [] for hospital in hospitals.keys()}
    proposals = {resident: 0 for resident in free_residents}
    
    # Create inverse preference lists
    hospital_rankings = {}
    for hospital, prefs in hospitals.items():
        hospital_rankings[hospital] = {resident: rank for rank, resident in enumerate(prefs)}
    
    while free_residents:
        resident = free_residents[0]
        
        if proposals[resident] >= len(residents[resident]):
            free_residents.pop(0)
            continue
        
        hospital = residents[resident][proposals[resident]]
        proposals[resident] += 1
        
        current_assignment = assignments[hospital]
        
        if len(current_assignment) < hospital_capacities[hospital]:
            # Hospital has capacity, assign resident
            assignments[hospital].append(resident)
            free_residents.pop(0)
        else:
            # Hospital is full, check if resident is better than worst current resident
            # Find worst resident at this hospital
            worst_resident = None
            worst_rank = -1
            
            for r in current_assignment:
                rank = hospital_rankings[hospital][r]
                if rank > worst_rank:
                    worst_rank = rank
                    worst_resident = r
            
            # Compare with new resident
            new_rank = hospital_rankings[hospital][resident]
            
            if new_rank < worst_rank:
                # New resident is better, replace worst
                assignments[hospital].remove(worst_resident)
                assignments[hospital].append(resident)
                free_residents.pop(0)
                free_residents.append(worst_resident)
            # Else: hospital prefers current residents, resident remains free
    
    return assignments


def student_school_matching(students, schools, school_capacities):
    """
    Student-School Matching Problem.
    Similar to hospital-resident matching.
    
    Args:
        students: Dict mapping student -> list of schools (preferences)
        schools: Dict mapping school -> list of students (preferences)
        school_capacities: Dict mapping school -> capacity
    
    Returns:
        Dict mapping school -> list of students
    """
    return hospital_resident_matching(students, schools, school_capacities)


def demonstrate_applications():
    """Demonstrate various applications of stable matching"""
    print("=" * 60)
    print("Applications of Stable Matching")
    print("=" * 60)
    
    # Application 1: Hospital-Resident Matching
    print("\nApplication 1: Hospital-Resident Matching (Medical Residency)")
    print("-" * 60)
    
    residents = {
        'R1': ['H1', 'H2', 'H3'],
        'R2': ['H2', 'H1', 'H3'],
        'R3': ['H1', 'H3', 'H2'],
        'R4': ['H3', 'H1', 'H2'],
        'R5': ['H2', 'H3', 'H1']
    }
    
    hospitals = {
        'H1': ['R1', 'R3', 'R2', 'R4', 'R5'],
        'H2': ['R2', 'R5', 'R1', 'R3', 'R4'],
        'H3': ['R4', 'R3', 'R1', 'R2', 'R5']
    }
    
    capacities = {
        'H1': 2,
        'H2': 2,
        'H3': 1
    }
    
    print("Residents:")
    for resident, prefs in residents.items():
        print(f"  {resident}: {prefs}")
    
    print("\nHospitals (with capacities):")
    for hospital, prefs in hospitals.items():
        print(f"  {hospital} (capacity {capacities[hospital]}): {prefs}")
    
    assignments = hospital_resident_matching(residents, hospitals, capacities)
    
    print("\nFinal Assignments:")
    for hospital, assigned_residents in sorted(assignments.items()):
        print(f"  {hospital}: {assigned_residents}")
    
    # Application 2: Student-School Matching
    print("\n\nApplication 2: Student-School Matching")
    print("-" * 60)
    
    students = {
        'S1': ['School_A', 'School_B', 'School_C'],
        'S2': ['School_B', 'School_A', 'School_C'],
        'S3': ['School_A', 'School_C', 'School_B'],
        'S4': ['School_C', 'School_B', 'School_A'],
        'S5': ['School_B', 'School_C', 'School_A'],
        'S6': ['School_A', 'School_B', 'School_C']
    }
    
    schools = {
        'School_A': ['S1', 'S3', 'S6', 'S2', 'S4', 'S5'],
        'School_B': ['S2', 'S5', 'S1', 'S4', 'S3', 'S6'],
        'School_C': ['S4', 'S3', 'S1', 'S5', 'S2', 'S6']
    }
    
    school_capacities = {
        'School_A': 2,
        'School_B': 2,
        'School_C': 2
    }
    
    print("Students:")
    for student, prefs in students.items():
        print(f"  {student}: {prefs}")
    
    print("\nSchools (with capacities):")
    for school, prefs in schools.items():
        print(f"  {school} (capacity {school_capacities[school]}): {prefs}")
    
    school_assignments = student_school_matching(students, schools, school_capacities)
    
    print("\nFinal Assignments:")
    for school, assigned_students in sorted(school_assignments.items()):
        print(f"  {school}: {assigned_students}")
    
    # Application 3: Job Matching (one-to-one)
    print("\n\nApplication 3: Job-Applicant Matching (One-to-One)")
    print("-" * 60)
    
    applicants = {
        'Alice': ['Job1', 'Job2', 'Job3'],
        'Bob': ['Job2', 'Job1', 'Job3'],
        'Charlie': ['Job1', 'Job3', 'Job2']
    }
    
    jobs = {
        'Job1': ['Alice', 'Charlie', 'Bob'],
        'Job2': ['Bob', 'Alice', 'Charlie'],
        'Job3': ['Charlie', 'Alice', 'Bob']
    }
    
    print("Applicants:")
    for applicant, prefs in applicants.items():
        print(f"  {applicant}: {prefs}")
    
    print("\nJobs:")
    for job, prefs in jobs.items():
        print(f"  {job}: {prefs}")
    
    job_matching = gale_shapley(applicants, jobs)
    
    print("\nFinal Matching:")
    for job, applicant in sorted(job_matching.items()):
        print(f"  {job} <-> {applicant}")
    
    # Summary
    print("\n\n" + "=" * 60)
    print("Key Takeaways:")
    print("=" * 60)
    print("1. Stable matching ensures no blocking pairs exist")
    print("2. Gale-Shapley algorithm guarantees a stable matching")
    print("3. The algorithm can be extended to many-to-one matching")
    print("4. Applications include:")
    print("   - Medical residency matching (NRMP)")
    print("   - School choice programs")
    print("   - Job placement")
    print("   - Organ donation matching")
    print("   - Network resource allocation")


if __name__ == "__main__":
    demonstrate_applications()
