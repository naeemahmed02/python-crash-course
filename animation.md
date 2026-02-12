# 1️⃣ Introduction to Animation in Web Design

Animation in web design means changing an element’s appearance or position over time.

With CSS3, we can animate:

* Position
* Size
* Color
* Opacity
* Rotation
* Scale
* And much more

CSS animations are:

* Lightweight
* Faster than JavaScript in many cases
* GPU accelerated (smooth on modern devices)

---

# 2️⃣ Types of CSS Animations

There are **two main ways** to create animation in CSS:

### 1. CSS Transitions

### 2. CSS Keyframe Animations

---

# 3️⃣ CSS Transitions (Basic Animation)

A transition creates smooth change between two states.

Usually triggered by:

* `:hover`
* `:focus`
* `:active`
* Class change (via JavaScript)

---

## ✅ Basic Syntax

```css
element {
  transition: property duration timing-function delay;
}
```

---

## ✅ Example 1: Hover Color Change

```html
<button class="btn">Hover Me</button>
```

```css
.btn {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  transition: background-color 0.5s ease;
}

.btn:hover {
  background-color: red;
}
```

🔎 Explanation:

* When user hovers
* Background smoothly changes in 0.5 seconds

---

## Transition Properties

| Property                   | Description               |
| -------------------------- | ------------------------- |
| transition-property        | Which property to animate |
| transition-duration        | How long animation runs   |
| transition-timing-function | Speed curve               |
| transition-delay           | Delay before start        |

---

## Timing Functions

| Value       | Effect                            |
| ----------- | --------------------------------- |
| linear      | Constant speed                    |
| ease        | Slow start, fast middle, slow end |
| ease-in     | Slow start                        |
| ease-out    | Slow end                          |
| ease-in-out | Slow start & end                  |

---

# 4️⃣ CSS Keyframe Animations (Advanced)

Transitions move from **state A → state B**

Keyframes allow:

* Multiple steps
* Complex motion
* Automatic animation
* Looping

---

## ✅ Basic Structure

### Step 1: Define Keyframes

```css
@keyframes animationName {
  from { }
  to { }
}
```

OR

```css
@keyframes animationName {
  0%   { }
  50%  { }
  100% { }
}
```

---

### Step 2: Apply Animation

```css
element {
  animation: animationName duration;
}
```

---

# 5️⃣ Example: Moving Box

```html
<div class="box"></div>
```

```css
.box {
  width: 100px;
  height: 100px;
  background: green;

  animation: moveRight 2s infinite alternate;
}

@keyframes moveRight {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(300px);
  }
}
```

🔎 Explanation:

* 2 seconds duration
* infinite → repeats forever
* alternate → moves back and forth

---

# 6️⃣ Animation Properties (Detailed)

| Property                  | Description                |
| ------------------------- | -------------------------- |
| animation-name            | Name of keyframe           |
| animation-duration        | Time animation runs        |
| animation-delay           | Delay before starting      |
| animation-iteration-count | Number of repeats          |
| animation-direction       | normal, reverse, alternate |
| animation-timing-function | Speed curve                |
| animation-fill-mode       | Keeps final state          |
| animation-play-state      | running / paused           |

---

## Example with All Properties

```css
.box {
  animation-name: bounce;
  animation-duration: 3s;
  animation-delay: 1s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-timing-function: ease-in-out;
}
```

---

# 7️⃣ Transformations (Very Important for Animation)

Most animations use `transform`.

## Common Transform Functions

| Function        | Effect       |
| --------------- | ------------ |
| translate(x, y) | Move element |
| scale(x, y)     | Resize       |
| rotate(deg)     | Rotate       |
| skew(x, y)      | Skew element |

---

## Example: Rotate

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

.loader {
  animation: spin 2s linear infinite;
}
```

---

# 8️⃣ Opacity Animation (Fade In)

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.text {
  animation: fadeIn 2s ease-in;
}
```

Used for:

* Page loading
* Modal windows
* Text appearance

---

# 9️⃣ Combining Multiple Animations

```css
.box {
  animation: move 2s infinite alternate,
             colorChange 3s infinite;
}
```

You can apply multiple animations to one element.

---

# 🔟 Real-World Use Cases

✔ Buttons hover effects
✔ Loading spinners
✔ Image sliders
✔ Navigation menu slide
✔ Card hover animations
✔ Notification popups
✔ Background animations

---

# 1️⃣1️⃣ Animation Performance Tips (Important for Students)

### ✅ Use transform instead of top/left

Bad:

```css
left: 100px;
```

Good:

```css
transform: translateX(100px);
```

Why?

* Transform uses GPU
* Smoother performance

---

### ✅ Use opacity for fade effects

It’s faster than changing display.

---

### ✅ Avoid heavy animation on mobile

Keep animations:

* Short
* Smooth
* Lightweight

---

# 1️⃣2️⃣ Difference Between Transition and Animation

| Transition         | Animation               |
| ------------------ | ----------------------- |
| Needs trigger      | Can run automatically   |
| Only start → end   | Multiple stages         |
| Simple effects     | Complex motion          |
| Short interactions | Advanced visual effects |

---

# 1️⃣3️⃣ Mini Student Project Example

Create a button with:

* Hover grow effect
* Click bounce effect

```css
.button {
  padding: 12px 25px;
  background: purple;
  color: white;
  transition: transform 0.3s ease;
}

.button:hover {
  transform: scale(1.1);
}

.button:active {
  animation: bounce 0.4s;
}

@keyframes bounce {
  0%   { transform: scale(1); }
  50%  { transform: scale(0.9); }
  100% { transform: scale(1); }
}
```

---

# 1️⃣4️⃣ Summary

CSS3 Animation allows you to:

* Create smooth UI effects
* Improve user experience
* Replace JavaScript for simple animations
* Build interactive and modern websites

Main concepts students must remember:

1. Transition = simple state change
2. Keyframes = complex animation
3. Transform + Opacity = best performance
4. Use animation properties properly
5. Keep animations smooth and meaningful

---
