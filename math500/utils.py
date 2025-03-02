from lm_eval.tasks.math500 import grader
from lm_eval.tasks.math500 import math_normalize
import re

def normalize_answer(answer):
    return math_normalize.normalize_answer(answer)

def process_problem(problem):
    ground_truth = problem.get("answer")
    return {
        "ground_truth": normalize_answer(ground_truth),
        "problem": problem["problem"],
    }

def process_gt(gt):
    return normalize_answer(gt)

def process_generated_answer(answer):
    return normalize_answer(answer)

def extract_boxed_value(s):
    match = re.search(r'\\boxed\{(.*)\}', s)
    if match:
        return match.group(1).strip() 
    else:
        return "No answer found."

def calculate_math_accuracy(*args, **kwargs):
    '''
    if args:
        # 调用方式为 calculate_math_accuracy([golden, generated])
        if len(args) == 1 and isinstance(args[0], list) and len(args[0]) == 2:
            golden = args[0][0]
            generated = args[0][1]
        else:
            raise ValueError("Unexpected arguments passed")
    elif "references" in kwargs and "predictions" in kwargs:
        # 调用方式为 calculate_math_accuracy(references=[golden], predictions=[generated])
        if kwargs["references"] and kwargs["predictions"]:
            golden = kwargs["references"][0]
            generated = kwargs["predictions"][0]
        else:
            raise ValueError("Empty references or predictions")
    else:
        raise ValueError("Invalid arguments passed")

    processed_gold = process_gt(golden)
    processed_generated = process_generated_answer(generated)
    return grader.grade_answer(processed_generated, processed_gold)
    '''

# 在每一次输入内检索golden和generated，在这里和被注释代码等效
    if kwargs["references"] and kwargs["predictions"]:
        scores = []
        for golden, generated in zip(kwargs["references"], kwargs["predictions"]):
            print("//")
            print("golden: ", golden)
            print("generated: ", generated)
            processed_gold = process_gt(golden)
            answer=extract_boxed_value(generated)
            # print("answer: ", answer)
            processed_generated = process_generated_answer(answer)
            print("processed_generated: ", processed_generated)
            score = grader.grade_answer(processed_generated, processed_gold)
            scores.append(score)
        return scores
    else:
        print("error")


def aggregate_scores(input):
    return sum([sum(i) for i in input]) / sum([len(j) for j in input])