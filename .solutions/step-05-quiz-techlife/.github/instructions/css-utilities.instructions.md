---
description: CSS utility classes and styling practices for this Python/Jinja2 project.
---

# CSS Styling Practices

## Overview
This project uses custom CSS utility classes (similar to Tailwind) defined in `app/static/css/app.css`. These provide consistent, composable styling without external dependencies.

## Available Utilities

### Layout
```css
.flex, .flex-col, .flex-1
.grid, .grid-cols-5
.items-center, .justify-center, .justify-between
```

### Spacing
```css
.p-1 through .p-6, .px-*, .py-*
.mb-2 through .mb-8, .mx-auto
.gap-1, .space-y-2
```

### Sizing
```css
.h-full, .w-full, .min-h-full
.max-w-xs, .max-w-sm, .max-w-md
.aspect-square
```

### Colors
```css
.bg-white, .bg-gray-50, .bg-gray-100
.bg-accent (primary blue), .bg-marked (green for selected)
.text-gray-500 through .text-gray-900
.text-green-600, .text-amber-500
```

### Typography
```css
.text-xs through .text-5xl
.font-semibold, .font-bold
.text-center, .text-left
.leading-tight
```

### Borders & Shadows
```css
.border, .border-b
.rounded, .rounded-lg, .rounded-xl
.shadow-sm, .shadow-xl
```

### Positioning
```css
.fixed, .absolute, .relative
.inset-0, .z-50
```

### Animation
```css
.transition-all, .transition-colors
.duration-150
.animate-[bounce_0.5s_ease-out]
```

## Best Practices

1. **Compose utilities**: Combine classes for complex layouts
2. **Add new utilities to app.css**: When needed, follow existing patterns
3. **Use CSS variables**: For theming, define in `:root`
4. **Keep specificity low**: Utility classes should be single-purpose

## Example Component Styling
```html
<div class="flex flex-col items-center justify-center min-h-full bg-gray-50">
    <button class="px-6 py-3 bg-accent text-white rounded-lg font-semibold">
        Start Game
    </button>
</div>
```