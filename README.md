# Personal Portfolio Website

A responsive personal portfolio website built with HTML, CSS, and Bootstrap 5.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Multi-page Structure**: Homepage, About, Resume, Projects, and Contact pages
- **Contact Form**: Fully validated form with password confirmation
- **Accessibility**: Screen reader friendly with proper ARIA labels and semantic HTML
- **Bootstrap Integration**: Uses Bootstrap 5.3.2 for responsive components

## Project Structure

```
├── index.html          # Homepage
├── about.html          # About Me page
├── resume.html         # Resume/CV page
├── projects.html       # Projects showcase
├── contact.html        # Contact form page
├── thankyou.html       # Thank you page after form submission
├── styles.css          # Custom CSS styles
├── images/             # Image assets directory
├── .prompt/            # AI development notes
│   └── dev_notes.md    # AI prompts and reflection
└── README.md           # This file
```

## Setup Instructions

1. **Clone or Download** the project files to your local machine
2. **Add Images**: Place your profile photo as `images/profile.jpg` (recommended size: 400x400px)
3. **Add Project Screenshots**: Add project images to the `images/` directory:
   - `project1-screenshot.jpg`
   - `project2-screenshot.jpg` 
   - `project3-screenshot.jpg`
4. **Customize Content**: 
   - Replace "John Doe" with your name throughout all HTML files
   - Update contact information (email, phone, LinkedIn, GitHub)
   - Add your actual project descriptions and links
   - Update the resume content with your experience and education
5. **Test the Website**: Open `index.html` in your web browser

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Technologies Used

- **HTML5**: Semantic markup and form validation
- **CSS3**: Custom styling, animations, and responsive design
- **Bootstrap 5.3.2**: Responsive framework and components
- **Font Awesome 6.4.0**: Icons and visual elements
- **JavaScript**: Form validation and interactive features

## Form Validation Features

The contact form includes:
- Required field validation
- Email format validation
- Password strength requirements (minimum 8 characters)
- Password confirmation matching
- Real-time validation feedback
- Accessibility-compliant labels and error messages

## AI-Assisted Development

This project was developed using AI assistance (Cursor) as part of an AI-first development course. See `.prompt/dev_notes.md` for detailed documentation of AI prompts used and development reflection.

## Customization Tips

1. **Colors**: Modify CSS custom properties in `styles.css` to change the color scheme
2. **Fonts**: Update the font-family in CSS variables to use your preferred fonts
3. **Layout**: Adjust Bootstrap grid classes for different layouts
4. **Animations**: Modify CSS animations for different effects
5. **Content**: All content is easily editable in the HTML files

## Future Enhancements

- Add a blog section
- Implement dark mode toggle
- Add more interactive animations
- Integrate with a backend for form handling
- Add a portfolio filter system
- Implement lazy loading for images

---

**Note**: This is a static website that can be hosted on any web server or GitHub Pages.
