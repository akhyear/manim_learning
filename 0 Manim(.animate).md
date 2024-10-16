### **List of Animatable Methods:**

1. **`rotate(angle)`**:  
   * Rotates the object by the specified `angle` (in radians).  
2. **`shift(direction)`**:  
   * Moves the object in a specific direction (e.g., `UP`, `DOWN`, `LEFT`, `RIGHT`, or custom vector).  
3. **`scale(factor)`**:  
   * Resizes the object by the given scaling `factor`. For example, `scale(2)` makes it twice as large.  
4. **`move_to(target_position)`**:  
   * Moves the object to a new `target_position` on the screen.  
5. **`set_color(new_color)`**:  
   * Changes the color of the object to `new_color` (e.g., `RED`, `GREEN`, etc.).  
6. **`set_opacity(opacity)`**:  
   * Adjusts the transparency of the object. `opacity=1` means fully opaque, and `opacity=0` means fully transparent.  
7. **`set_fill(color, opacity)`**:  
   * Sets both the `fill color` and `opacity` of the inside of the object.  
8. **`set_stroke(color, width)`**:  
   * Sets the `stroke color` (border color) and `stroke width` of the object's outline.  
9. **`fade_in()` / `fade_out()`**:  
   * Makes the object gradually appear (`fade_in()`) or disappear (`fade_out()`).  
10. **`next_to(mobject, direction)`**:  
    * Moves the object next to another object (`mobject`) in a specific direction (e.g., `RIGHT`, `LEFT`).  
11. **`stretch(factor, dim)`**:  
    * Stretches the object by `factor` in a specific `dimension` (e.g., `dim=0` for horizontal or `dim=1` for vertical).  
12. **`flip(axis)`**:  
    * Flips (mirrors) the object across a given axis (e.g., horizontal or vertical).  
13. **`set_height(height)`**:  
    * Changes the height of the object to the specified value.  
14. **`set_width(width)`**:  
    * Changes the width of the object to the specified value.  
15. **`match_height(target_object)`**:  
    * Adjusts the height of the object to match that of another `target_object`.  
16. **`match_width(target_object)`**:  
    * Adjusts the width of the object to match that of another `target_object`.  
17. **`match_color(target_object)`**:  
    * Changes the color of the object to match that of another `target_object`.  
18. **`to_edge(direction)`**:  
    * Moves the object to the edge of the screen in a specific `direction` (e.g., `UP`, `DOWN`, `LEFT`, `RIGHT`).  
19. **`to_corner(direction)`**:  
    * Moves the object to a corner of the screen, like `UP_LEFT` or `DOWN_RIGHT`.  
20. **`align_to(mobject, direction)`**:  
    * Aligns the object to another `mobject` along a specific `direction`.  
21. **`set_sheen(direction, factor)`**:  
    * Adds a shiny effect in a `direction` with a specified intensity (`factor`).  
22. **`set_background_stroke(color, width)`**:  
    * Changes the stroke (outline) of the background of the object, with a specified `color` and `width`.  
23. **`round_corners(radius)`**:  
    * Rounds the corners of the object by the specified `radius`.  
24. **`become(target_object)`**:  
    * Transforms the object into another `target_object` by copying its shape and size.  
25. **`set_z_index(z_index)`**:  
    * Changes the `z-index` (layering order) of the object, affecting its appearance relative to other objects.

Here are additional aspects of controlling animations in **Manim**, beyond just duration and easing functions:

1. **`run_time`**:  
   * Specifies the **duration** of the animation in seconds (how long the animation takes to complete). Example: `run_time=3` makes the animation last 3 seconds.  
2. **`rate_func`**:  
   * Defines the **easing function** or how the animation progresses over time. Common `rate_func` options:  
     * `smooth`: The animation starts slow, speeds up in the middle, and slows down at the end.  
     * `linear`: The animation progresses at a constant speed.  
     * `there_and_back`: The animation goes forward and then returns to its original state.  
     * `ease_in_out`: Starts slow, speeds up, and then slows down.  
3. **`lag_ratio`**:  
   * Controls the **delay** between starting animations on different objects. If multiple objects are being animated at once, `lag_ratio` determines how much time passes before each object starts animating. Example: `lag_ratio=0.5` means the second object starts animating halfway through the first object's animation.  
4. **`wait_time`**:  
   * Adds a **pause** before starting the next animation, allowing for a moment of stillness between animations.  
5. **`reverse`**:  
   * Plays the animation in **reverse**. Instead of going from start to end, it goes from end to start.  
6. **`about_point`**:  
   * Defines a **reference point** around which certain transformations (like rotation or scaling) should occur. Example: `rotate(PI, about_point=ORIGIN)` will rotate an object around the origin rather than its center.  
7. **`about_edge`**:  
   * Similar to `about_point`, but specifies a specific **edge** of the object (e.g., `LEFT`, `RIGHT`, `UP`, `DOWN`) to use as the reference for certain transformations.  
8. **`submobject_mode`**:  
   * Applies the animation to the **subcomponents** of an object, such as letters in a text object or segments in a graph, individually rather than animating the whole object at once.  
9. **`rate_func` combinations**:  
   * You can create **custom easing functions** by combining or modifying existing `rate_func` functions. Example: `rate_func=lambda t: t**2` for quadratic easing.  
10. **`path_arc`**:  
    * Specifies an **arc** along which an object should move or rotate. For example, `path_arc=PI/4` makes an object follow a quarter-circle path during the animation.  
11. **`overlapping_animation`**:  
    * When multiple animations affect the same object, this determines how they **overlap** or merge. You can decide if they should happen together or sequentially.

### **Summary:**

These parameters allow fine-tuned control over how animations behave, from pacing and delays to specific reference points for transformations, giving you a lot of flexibility in designing your animations.

