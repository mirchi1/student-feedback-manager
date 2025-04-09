def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == "__main__":
    sample_scores = [70, 80, 90]
    print(f"Average score: {calculate_average(sample_scores)}") 
