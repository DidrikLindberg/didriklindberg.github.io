# Dark Mode Feature Documentation

## Overview
Comprehensive dark mode implementation for the A-frame Solutions marketing website, providing users with a toggle to switch between light and dark themes across all pages.

## Feature Details

### User-Facing Features
- **Toggle Button**: Sun/moon icon in navigation bar (both desktop and mobile views)
- **Persistent Preference**: User's theme choice is saved and remembered across sessions
- **System Detection**: Automatically respects user's system dark mode preference on first visit
- **Instant Switching**: Seamless theme switching without page reload
- **Universal Coverage**: Dark mode works on all pages (home, services, projects, about, contact)

### Technical Implementation

#### 1. Tailwind CSS Configuration
- Enabled class-based dark mode in Tailwind config (`base.html:20`)
- Uses `dark:` utility classes throughout all templates

#### 2. FOUC Prevention
- Initialization script runs before page render (`base.html:50-59`)
- Checks localStorage for saved preference
- Falls back to system preference if no saved choice
- Applies `dark` class to `<html>` element immediately

#### 3. Toggle UI Components
**Desktop Toggle** (`base.html:144-157`)
- Icon button with sun/moon SVG icons
- Located in main navigation bar
- Hover states and focus rings for accessibility

**Mobile Toggle** (`base.html:199-216`)
- Full-width button in mobile menu
- Text label "Dark Mode" with icon
- Consistent styling with other mobile menu items

#### 4. JavaScript Logic (`base.html:338-377`)
```javascript
// Theme state management
- Reads current theme from localStorage
- Toggles 'dark' class on html element
- Saves preference to localStorage
- Updates icon visibility
- Handles both desktop and mobile toggles
```

#### 5. Color System
All templates follow consistent dark mode color patterns:

**Backgrounds:**
- `bg-white dark:bg-gray-800` - Primary containers
- `bg-gray-50 dark:bg-gray-900` - Alternate sections
- `bg-gray-900 dark:bg-gray-950` - Hero sections

**Text:**
- `text-gray-900 dark:text-white` - Headings
- `text-gray-700 dark:text-gray-300` - Body text
- `text-gray-600 dark:text-gray-400` - Muted/secondary text

**Interactive Elements:**
- `text-primary-600 dark:text-primary-400` - Links and buttons
- `hover:text-primary-800 dark:hover:text-primary-300` - Hover states

**Borders & Dividers:**
- `border-gray-200 dark:border-gray-700` - Standard borders
- `border-gray-100 dark:border-gray-700` - Subtle borders

### Files Modified

1. **templates/base.html**
   - Added Tailwind dark mode configuration
   - Implemented FOUC prevention script
   - Added toggle buttons (desktop & mobile)
   - Added JavaScript toggle logic
   - Updated navigation styles
   - Updated footer styles

2. **templates/home.html**
   - Hero section gradients
   - Certifications bar
   - Services overview cards
   - Why Choose Us section
   - Featured projects cards
   - Testimonials section
   - CTA sections

3. **templates/services.html**
   - Hero section
   - Service cards with details
   - Engagement models section
   - All text and backgrounds

4. **templates/service_detail.html**
   - Hero section with back link
   - Service details section
   - Deliverables and outcomes lists
   - CTA section

5. **templates/projects.html**
   - Hero section
   - Project cards grid
   - All text and badges

6. **templates/project_detail.html**
   - Hero with breadcrumb
   - Challenge, solution, results sections
   - Tech stack badges
   - CTA section

7. **templates/about.html**
   - Hero section
   - Company story content

8. **templates/contact.html**
   - Already had dark mode support
   - Verified consistency

### Browser Compatibility
- Works in all modern browsers supporting localStorage and CSS custom properties
- Graceful degradation in older browsers (defaults to light mode)
- No JavaScript errors if localStorage is unavailable

### Accessibility Considerations
- Toggle buttons have proper ARIA labels
- Sufficient color contrast in both themes (meets WCAG AA standards)
- Focus indicators visible in both modes
- Icon changes clearly indicate current state

### Testing Checklist
- [x] Toggle works on desktop navigation
- [x] Toggle works on mobile navigation
- [x] Preference persists across page navigation
- [x] Preference persists after browser refresh
- [x] System preference detected on first visit
- [x] All pages styled correctly in light mode
- [x] All pages styled correctly in dark mode
- [x] No FOUC when loading pages
- [x] Icons update correctly when toggling
- [x] Hover states work in both modes
- [x] Form inputs readable in both modes

## Future Enhancements (Optional)
- Add transition animations for smoother color changes
- Add keyboard shortcut for power users
- Add theme preview in settings page
- Implement auto-switching based on time of day
- Add more theme options (e.g., high contrast mode)

## Maintenance Notes
When adding new content or pages:
1. Always include `dark:` variants for all colored elements
2. Follow the color patterns documented in CLAUDE.md
3. Test both light and dark modes before committing
4. Ensure sufficient contrast in both themes

## Resources
- [Tailwind CSS Dark Mode Documentation](https://tailwindcss.com/docs/dark-mode)
- [MDN localStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [WCAG Color Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
