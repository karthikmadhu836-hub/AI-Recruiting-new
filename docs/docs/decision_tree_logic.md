# Decision Tree Logic

## Objective

Provide adaptive interview questioning based on candidate response quality.

## Flow

START

↓

Ask Question

↓

Capture Answer

↓

Analyze Answer Quality

↓

| Condition | Action          |
| --------- | --------------- |
| Empty     | Retry           |
| Too Short | Ask Elaboration |
| Uncertain | Clarify         |
| Basic     | Ask Example     |
| Good      | Continue        |

↓

Adapt Question Difficulty

↓

| Quality                | Difficulty |
| ---------------------- | ---------- |
| Empty                  | Simplify   |
| Too Short              | Simplify   |
| Basic                  | Example    |
| Good + High Confidence | Advanced   |

↓

Generate Follow-Up

↓

Update Conversation State

↓

Next Question / End

## Benefits

* Dynamic interviews
* Human-like conversation flow
* Better candidate evaluation
* Reduced repetitive questioning
