# Skilift

## Description
```
﻿

You arrive at the base station of a ski lift. 
Unfortunately for you, the lift is not in operation but you have to reach the next summit somehow. 
You enter the control room to find a control terminal with the words "Please input your key:"
```

## Provided Files
`top.v`

## Writeup

First I started by inspecting the verilog script. <br/>
```v
module top(
    input [63:0] key,
    output lock
);
  
    reg [63:0] tmp1, tmp2, tmp3, tmp4;

    // Stage 1
    always @(*) begin
        tmp1 = key & 64'hF0F0F0F0F0F0F0F0;
    end
    
    // Stage 2
    always @(*) begin
        tmp2 = tmp1 <<< 5;
    end
    
    // Stage 3
    always @(*) begin
        tmp3 = tmp2 ^ "HACKERS!";
    end

    // Stage 4
    always @(*) begin
        tmp4 = tmp3 - 12345678;
    end

    // I have the feeling "lock" should be 1'b1
    assign lock = tmp4 == 64'h5443474D489DFDD3;

endmodule
```

Also connecting to the service we get asked for a `key` in `hex`. <br/>
I could easily deduct that we can reverse the `key` because we basically always have equations with only 1 missing variable, but to solve it I first converted it to python code. <br/>
```py
def solve_key(tmp4):
    # Stage 4
    tmp3 = tmp4 + 12345678

    # Stage 3
    tmp2 = tmp3 ^ int("HACKERS!".encode("utf-8").hex(), 16)

    # Stage 2
    tmp1 = tmp2 >> 5

    # Stage 1
    key = tmp1 | ~0xF0F0F0F0F0F0F0F0

    print(hex(key))

solve_key(0x5443474D489DFDD3)
```

Like this I got the key for the service. <br/>
Connecting to it now using netcat I got the flag `gctf{V3r1log_ISnT_SO_H4rd_4fTer_4ll_!1!}` which concludes this challenge.