import sys

def largest_number_of_faked_topics(topics):
    """
    Finds the largest number of topics that could have possibly been faked.

    Args:
        topics (list[str]): List of topics to check for fake topics.

    Returns:
        int: The largest number of fake topics in the list.
    """
    # Initialize a counter for the total number of fake topics
    num_fake_topics = 0

    # Iterate through each topic in the list
    for i in range(len(topics)):
        # Check if the current topic is already on the sheet
        if topics[i] in topics:
            # If it is, then it cannot be a fake topic
            continue
        else:
            # Otherwise, check if any of the other topics can be used to form this topic
            for j in range(len(topics)):
                # Check if the current topic is already on the sheet
                if topics[j] in topics:
                    # If it is, then it cannot be a fake topic
                    continue
                else:
                    # Otherwise, check if the other topic can be used to form this topic
                    if " ".join([topics[i], topics[j]]) in topics:
                        # If it can, then increase the number of fake topics by 1
                        num_fake_topics += 1

    return num_fake_topics

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(test_cases):
        N = int(input())
        topics = []
        for _ in range(N):
            topic = input().split()
            topics.append(" ".join(topic))
        print(f"Case #{case+1}: {largest_number_of_faked_topics(topics)}")