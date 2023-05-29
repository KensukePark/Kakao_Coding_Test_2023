def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries.reverse()
    pickups = pickups.reverse()
    delivery_amount = 0
    pickup_amount = 0
    for i in range(n):
        delivery_amount += deliveries[i]
        pickup_amount += pickups[i]
        while True:
            delivery_amount -= cap
            pickup_amount -= cap
            answer += (n - i) * 2
            if delivery_amount == 0 and pickup_amount == 0:
                break
    return answer
