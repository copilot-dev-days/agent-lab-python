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
/* Padding */
.p-1, .p-3, .p-4, .p-6
.px-3, .px-4, .px-6, .px-8
.py-1\.5, .py-2, .py-3, .py-4
/* Margin */
.mb-2, .mb-3, .mb-4, .mb-6, .mb-8, .mx-auto
/* Gap */
.gap-1, .space-y-2
```

### Sizing
```css
.h-full, .w-full, .w-16, .min-h-full
.max-w-xs, .max-w-sm, .max-w-md
.aspect-square
.min-h-[60px]
```

### Colors
```css
/* Backgrounds */
.bg-white, .bg-gray-50, .bg-gray-100
.bg-amber-100, .bg-amber-200
.bg-accent (primary blue: #2563eb)
.bg-marked (light green: #dcfce7)
.bg-black/50 (semi-transparent overlay)
/* Text */
.text-white
.text-gray-500, .text-gray-600, .text-gray-700, .text-gray-800, .text-gray-900
.text-green-600, .text-green-800
.text-amber-500, .text-amber-800, .text-amber-900
```

### Typography
```css
/* Size (only these exist — no text-base, text-xl, text-2xl, etc.) */
.text-xs, .text-sm, .text-lg, .text-3xl, .text-4xl, .text-5xl
.font-semibold, .font-bold
.text-center, .text-left
.leading-tight
```

### Borders & Shadows
```css
.border, .border-b
.border-gray-200, .border-gray-300, .border-amber-400, .border-marked-border
.rounded, .rounded-lg, .rounded-xl
.shadow-sm, .shadow-xl
```

### Positioning
```css
.fixed, .absolute, .relative
.inset-0
.top-0\.5, .right-0\.5
.z-50
```

### Interactivity
```css
.select-none
.wrap-break-word
.hyphens-auto
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