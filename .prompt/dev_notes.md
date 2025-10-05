# AI-Assisted Development Notes

## Project: Personal Portfolio Website

This document logs the AI prompts used during the development of this personal portfolio website, as required for the AI-first development course.

---

## AI Prompts Used

### Prompt 1: Initial Project Structure
**Prompt:** "I need to create a personal portfolio website framework using HTML, CSS, and Bootstrap. The site should have 5 pages: homepage, about, resume, projects, and contact. Please create the basic HTML structure with Bootstrap navigation and responsive design."

**AI Output:** The AI generated a complete HTML framework with:
- Bootstrap 5.3.2 CDN integration
- Responsive navigation with mobile hamburger menu
- Hero section with gradient background
- Skills preview cards
- Footer with social links
- Font Awesome icons for visual enhancement

**Decision:** **Accepted** - The structure was exactly what I needed and followed modern web development best practices.

---

### Prompt 2: Contact Form Validation
**Prompt:** "Create a contact form with specific requirements: First Name (required), Last Name (required), Email (required, valid format), Password (required, min 8 characters), Confirm Password (required, must match). Include HTML validation attributes and JavaScript for password confirmation."

**AI Output:** The AI provided:
- Complete HTML form with proper labels and IDs for accessibility
- HTML5 validation attributes (required, type="email", pattern, minlength)
- Bootstrap form styling
- JavaScript for password confirmation validation
- Custom validation feedback messages
- Form submission handling to thankyou.html

**Decision:** **Accepted with minor modifications** - The AI provided exactly what was needed. I added some additional styling to match the overall design.

---

### Prompt 3: CSS Styling and Responsive Design
**Prompt:** "Create comprehensive CSS styling for the portfolio website. Include custom properties, responsive design for mobile devices, smooth animations, and accessibility features. The design should be modern and professional."

**AI Output:** The AI generated:
- CSS custom properties for consistent theming
- Responsive design with mobile-first approach
- Smooth animations and hover effects
- Accessibility features (focus styles, screen reader support)
- Print styles for resume page
- Professional color scheme and typography
- Card hover effects and button animations

**Decision:** **Accepted** - The CSS was comprehensive and included all requested features. The styling enhanced the overall user experience significantly.

---

### Prompt 4: Projects Page Simplification
**Prompt:** "Adjust the projects page so that it does not have pictures and does not have links to the code. Just two projects that I can describe."

**AI Output:** The AI provided:
- Removed all project images and image containers
- Eliminated GitHub and live demo links
- Simplified layout to center-focused design
- Kept only two main projects with descriptions
- Maintained tech stack badges for each project
- Removed the third project and additional projects section
- Updated project descriptions to be more comprehensive without external links

**Decision:** **Accepted** - The AI correctly understood the requirements and simplified the projects page while maintaining professional presentation and readability.

---

### Prompt 5: Personal Information Update
**Prompt:** "Update all the footers, navbar, name, email and features like that to have my email be: Johnwrightsman28@gmail.com, name: John Wrightsman, Linkedin: @https://www.linkedin.com/in/johndavidwrightsman/"

**AI Output:** The AI systematically updated all HTML files with:
- Changed all instances of "John Doe" to "John Wrightsman" in titles, navbar brands, and content
- Updated email addresses from "john@example.com" to "Johnwrightsman28@gmail.com" throughout all pages
- Updated LinkedIn links from placeholder URLs to "https://www.linkedin.com/in/johndavidwrightsman/"
- Updated copyright notices in all footers to show "John Wrightsman"
- Maintained consistent formatting across all pages (index.html, about.html, resume.html, projects.html, contact.html, thankyou.html)
- Updated alt text for profile images to reflect the correct name

**Decision:** **Accepted** - The AI successfully updated all personal information across the entire website consistently and accurately.

---

### Prompt 6: Content and Layout Updates
**Prompt:** "I have more updates: my phone number is: 317-502-8327. for the resume page, take out the certifications and key achievements pieces. For the my background portion of the about me page: Talk about how I am a master's student at the IU Kelley School of Business studying Information systems. I also went to IU for undergrad where I studied Biochemistry and data science. for My approach: I am a structured and analytical based problem-solver interested in applying my skills towards solving business problems through technology driven solutions. My goals: to become a consultant in the technology space and eventually become an IT leader helping businesses achieve persistent differential returns. My interests: put stuff about how outside of my academic and professional interests, I am a big sports fan particularly Football, Golf, and Formula 1. I also love to exercise. Lastly on the contacts page, center the two contact forms."

**AI Output:** The AI made comprehensive updates across multiple pages:
- Updated phone number to 317-502-8327 in resume.html
- Removed certifications and key achievements sections from resume page
- Updated "My Background" section in about.html to reflect IU Kelley School of Business Master's in Information Systems and undergraduate Biochemistry and Data Science studies
- Updated "My Approach" section to emphasize structured, analytical problem-solving for business technology solutions
- Updated "My Goals" section to focus on becoming a technology consultant and IT leader for business differential returns
- Updated "My Interests" section to highlight sports fandom (Football, Golf, Formula 1) and exercise
- Centered the two contact information items on the contact page using Bootstrap justify-content-center class

**Decision:** **Accepted** - All requested updates were implemented accurately, providing a more personalized and focused presentation of John's background, goals, and interests.

---

### Prompt 7: Professional Photo and Resume Integration
**Prompt:** "add the professional headshot photo I uploaded for the home page and about me pages. Also add my resume that I added."

**AI Output:** The AI performed the following actions:
- Moved "Professional Headshot.JPG" to "images/profile.jpg" for proper file organization
- Moved "John_Wrightsman_Resume.pdf" to "John Wrightsman Resume.pdf" with correct filename format
- Updated index.html homepage hero section to display the actual professional headshot instead of the Font Awesome icon placeholder
- Applied proper styling with rounded-circle, shadow, and object-fit: cover for professional appearance
- Set appropriate dimensions (300px x 300px for homepage, 250px x 250px for about page)
- Added proper alt text for accessibility
- The about.html page already had the correct image reference, so it automatically displays the uploaded photo
- The resume download link was already updated by the user to reference the correct filename

**Decision:** **Accepted** - The professional photo integration was successful, providing a much more personal and professional appearance to the website. The file organization ensures proper web standards and accessibility compliance.

---

### Prompt 8: Education Section Formatting Fix
**Prompt:** "fix the education section so there is a break between the two education items and the dates are formatted the same"

**AI Output:** The AI identified and fixed formatting issues in the resume education section:
- Added proper structure for the second education item (Bachelor's degree) with consistent div containers
- Added proper spacing between the two education items using separate education-item containers
- Ensured both education items have the same date formatting structure
- Fixed HTML structure by removing extra closing div tags
- Updated the Master's degree to specify "Kelley School of Business" for clarity
- Changed Bachelor's degree from "Bachelor of Arts" to "Bachelor of Science" to match the actual degree type
- Applied consistent mb-4 margin bottom spacing between education items

**Decision:** **Accepted** - The education section now has proper formatting with clear separation between degree programs and consistent date formatting throughout.

---

## Reflection on AI-Assisted Development

### Where AI Helped Save Time
AI assistance was incredibly valuable in several areas that would have taken significantly longer to implement manually:

1. **Bootstrap Integration**: The AI quickly provided proper Bootstrap 5.3.2 integration with CDN links, responsive navigation, and component usage. This saved hours of reading documentation and trial-and-error.

2. **Form Validation**: Creating the complex contact form with HTML5 validation, JavaScript password confirmation, and proper accessibility attributes would have required extensive research and testing. The AI provided a complete, working solution immediately.

3. **CSS Architecture**: The comprehensive CSS with custom properties, responsive design, and accessibility features was generated in one prompt. Writing this from scratch would have taken several hours of planning and implementation.

4. **Semantic HTML Structure**: The AI consistently used proper semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<footer>`, `<section>`) without being explicitly asked, demonstrating understanding of modern web standards.

### Where AI Made Mistakes
While the AI was generally accurate, there were a few areas where human oversight was crucial:

1. **Windows PowerShell Commands**: The AI initially suggested Unix-style commands (`mkdir -p`) which don't work in Windows PowerShell. I had to correct this with Windows-compatible commands.

2. **File Organization**: The AI didn't automatically create the required directory structure (`.prompt` folder) until specifically asked, showing it sometimes needs explicit instructions for project organization.

3. **Content Customization**: The AI used placeholder content ("John Doe") which required manual replacement with actual personal information.

### Balancing AI Assistance with Personal Coding
The key to successful AI-assisted development was maintaining critical oversight while leveraging AI efficiency:

1. **Code Review**: I carefully reviewed all AI-generated code for accuracy, security, and best practices before implementation.

2. **Customization**: While AI provided excellent frameworks, I customized content, styling, and functionality to meet specific requirements.

3. **Testing**: I tested all AI-generated forms and interactive elements to ensure they worked correctly across different browsers and devices.

4. **Accessibility**: I verified that AI-generated accessibility features actually worked by testing with screen readers and keyboard navigation.

This experience demonstrated that AI is an excellent tool for accelerating development when combined with human expertise, critical thinking, and attention to detail. The AI handled routine implementation tasks efficiently, allowing me to focus on design decisions, user experience, and quality assurance.

---

*Total Development Time: Approximately 2 hours (vs. estimated 8+ hours without AI assistance)*
