total_bottles   = 155 

bottles_per_box = 12 

 

complete_boxes  = total_bottles // bottles_per_box 

leftover        = total_bottles %  bottles_per_box 

 

print(f'Complete boxes : {complete_boxes}')  # 12 

print(f'Leftover bottles: {leftover}')        # 11 

 

# Floor division always rounds DOWN (towards negative infinity) 

print(-7 // 2)   # -4  (not -3!) 