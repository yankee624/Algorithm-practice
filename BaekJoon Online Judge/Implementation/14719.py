H, W = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
stack = []
idx = 0
while blocks[idx] == 0:
    idx += 1

if idx >= len(blocks):
    print(0)
else:
    while idx < len(blocks):
        curr_block = blocks[idx]
        if stack and curr_block > stack[-1][1]:
            # trap water
            prev_idx, prev_block = stack.pop()
            while stack and curr_block >= stack[-1][1]:
                prev_prev_idx, prev_prev_block = stack.pop()
                water += (idx - prev_prev_idx - 1) * (prev_prev_block - prev_block)
                prev_idx, prev_block = prev_prev_idx, prev_prev_block
            if stack:
                water += (idx - stack[-1][0] - 1) * (curr_block - prev_block)
        stack.append((idx, curr_block))
        idx += 1

    print(water)
