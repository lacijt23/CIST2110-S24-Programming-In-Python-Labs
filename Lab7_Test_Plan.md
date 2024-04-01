# 1 calculate_rectangle_area function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
001 | calculate_rectangle_area - Test with positive numbers | 3, 4 | 12 | 12 | Pass | N/A
002 | calculate_rectangle_area - Test with positive numbers | 5, 5 | 25 | 25 | Pass | N/A
003 | calculate_rectangle_area - Test with zeros | 0, 0 | 0 | 0 | Pass | N/A
004 | calculate_rectangle_area - Test with positive numbers | 10, 20 | 200 | 200 | Pass | N/A

## 2 calculate_hypotenuse function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
001 | calculate_hypotenus - Test with positive numbers | 3, 4 | 5 | 5 | Pass | N/A
002 | calculate_hypotenus - Test with positive numbers | 5, 12 | 13 | 16.4 | Fail | a**3 is causing an incorrect calculation
003 | calculate_hypotenus - Test with positive numbers (bugfix 002) | 5, 12 | 13 | 16.4 | Pass |
003 | calculate_hypotenus - Test with positive numbers | 7, 24 | 25 | 25 | Pass | N/A

## 3 test_is_even function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
001 | is_even - Test with even number | 2 | True | True | Pass | N/A
002 | is_even - Test with odd number | 7 | False | False | Pass | N/A

## 4 test_find_maximum function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
001 | find_maximum - Test with positive numbers | 3, 4 | 4 | 4 | Pass | N/A
002 | find_maximum - Test with positive numbers | 5, 12 | 12 | 12 | Pass | N/A

## 5 test_grade_calculator function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|---------------|
001 | grade_calculator - Test with positive numbers | 90 | A | A | Pass | N/A
002 | grade_calculator - Test with out of range upper bound | 105 | Invalid Score | Invalid Score | Pass | N/A