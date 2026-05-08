"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""
import os
# ============================================================
# Step 1: Read file contents
# ============================================================
notepath = os.path.join(os.getcwd(), "reviews.txt")

if os.path.exists(notepath):
    with open("reviews.txt" , "r") as file:
        content = file.read()
        #Total Characters
        total_Char = len(content)
        #Total Good and bad reviews
        bad_char = 0
        good_char = 0
        for char in content:
            if char.lower() == "good":
                good_char += 1
            if char.lower() == "bad":
                bad_char += 1
        #Total Reviews
        total_review = bad_char+good_char
        #percentage
        percent = good_char/total_review * 100
        #rating
        if percent >= 70:
            rating = "Positive"
        if percent >= 40:
            rating = "Mixed"
        else:
            rating = "Negative"
        
        print(rating)







