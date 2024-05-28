# Spinner

## Description
```
spin 10,000 times for flag
```

## Writeup

Starting off, I checked client-side JavaScript, which reveals a request being made after completing enough spins. <br/>

```js
const message = async () => {
  if (state.flagged) return;
  const element = document.querySelector(".message");
  element.textContent = Math.floor(state.total / 360);

  if (state.total >= 10_000 * 360) {
    state.flagged = true;
    const response = await fetch("/falg", { method: "POST" });
    element.textContent = await response.text();
  }
};
```

Seeing no kind of authentication required I tried to replicate the request using linux utility. <br/>
```sh
$ curl -X POST https://spinner.web.actf.co/falg
actf{b152d497db04fcb1fdf6f3bb64522d5e}
```


