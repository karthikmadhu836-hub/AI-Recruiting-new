# Sample Communication Score Outputs

## Example 1 – Strong Answer

Input:

I have experience in Python because I worked on backend systems.

Output:

{
"communication_score": 88.0,
"breakdown": {
"fluency": 1.0,
"grammar": 1.0,
"vocabulary": 0.8,
"clarity": 1.0,
"structure": 1.0,
"penalty": 0.1
}
}

---

## Example 2 – Average Answer

Input:

I worked with Python and SQL in projects.

Output:

{
"communication_score": 62.0,
"breakdown": {
"fluency": 0.6,
"grammar": 0.7,
"vocabulary": 0.6,
"clarity": 0.7,
"structure": 0.6,
"penalty": 0.2
}
}

---

## Example 3 – Weak Answer

Input:

Python project.

Output:

{
"communication_score": 38.0,
"breakdown": {
"fluency": 0.3,
"grammar": 0.4,
"vocabulary": 0.4,
"clarity": 0.4,
"structure": 0.4,
"penalty": 0.3
}
}
