# Midterm: LFTracer --- Line visit counter.
Midterm exam for 2024 Software Engineering.

## Requirements

* R1. Count the number of visiting for each statement in the target functions.
* R2. Write your `LFTracer.py` in the repository.
* R3. Test your `LFTracer.py` by using `pytest`.
* R4. You need to let your TA know your student ID and GitHub username together if necessary.
* R5. `LFTracer` class should be defined in the `LFTracer.py`
* R6. The above class is tested as:

```
def test_lf_sha256():
    with LFTracer(target_func = ["generate_hash", "_sigma0"]) as traced:
        encoded = "mysalt".encode()
        generate_hash(encoded).hex()

    answer1 = ...
    answer2 = ...
    assert traced.getLFMap() == answer1
    assert traced.getLFStat() == answer2
```

* R7. LFTracer should count the number of visiting for each statement in each target function.
      - The target functions should be specified by `target_func = ["func1", "func2"]`.
* R8. There should be a member function called “getLFMap()” in LFTracer, which returns a dictionary of {“func1”: {1: x1, 2: y1, ...}, “func2”: {1: x2, 2: y2, ...}, …}.
* R9. There should be a member function called "getLFStat()" in LFTracer, which returns a statistics of line visiting such as {"func1": {'num_visited_lines': ..., 'total_visitied_counts': ...}" 
* R10. "target_function" can be called multiple times.
* R11. To run some test cases given, you should install necessary pacakges listed in `requirements.txt`.

Note:

* N1. `pytest` (based on `test_lf1.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS are not accepted.
* N3. Late submissions are NOT allowed.
* N4. DO NOT change files in this repository except for `LVVTracer.py`. Adding new files are NOT allowed.



