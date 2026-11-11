"""
Batch Processor
Zecpath AI
"""


def batch_process(

    data,

    func
):

    return [

        func(item)

        for item in data
    ]


if __name__ == "__main__":

    numbers = [

        1,

        2,

        3
    ]

    result = batch_process(

        numbers,

        lambda x: x * 2
    )

    print(result)