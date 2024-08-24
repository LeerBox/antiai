
# Antiai - Script to generate outputs based on mathematical equations

import sys

def evaluate_equations(equations):
    results = []
    for equation in equations:
        try:
            result = eval(equation)
            results.append(f"{equation} = {result}")
        except Exception as e:
            results.append(f"Error evaluating equation '{equation}': {str(e)}")
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python antiai.py <equation1> <equation2> ...")
        sys.exit(1)

    equations = sys.argv[1:]
    results = evaluate_equations(equations)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
