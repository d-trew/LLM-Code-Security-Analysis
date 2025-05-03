T = int(input())
for _ in range(T):
    E, W = map(int, input().split())
    weights_needed = [list(map(int, input().split())) for _ in range(E)]
    operations = 0
    current_weights = []
    for exercise in weights_needed:
        new_weights = [weight for weight_type, weight in enumerate(exercise) if weight > 0]
        if not current_weights:
            current_weights = new_weights
        else:
            operations += sum(1 for _ in new_weights)
            current_weights = [weight for weight_type, weight in enumerate(current_weights + new_weights) if weight > 0]
    print(f"Case #{_+1}: {operations}")