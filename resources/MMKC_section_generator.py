template = '''<section class="img-section">
    <div class="{wrap_class}">
        <img class="img lazy" data-src="resources/MMKCMeetup-{num:02d}.jpg" loading="lazy" alt="MMKC Meetup {num:02d}">
    </div>
    <div class="{proj_info_class}">
        <span class="wrap"><h1 class="info-text">{num:02d}</h1></span>
        <span class="wrap"><h1 class="info-text">Keyboard</h1></span>
        <span class="wrap"><h1 class="info-text">Mumbai</h1></span>
        <span class="wrap"><h1 class="info-text">2024</h1></span>
        <span class="wrap"><h1 class="info-text">MMKC2024</h1></span>
    </div>
</section>'''

pattern = [1, 2]
sections = []
for i in range(1, 68):
    class_number = pattern[(i - 1) % 2]
    wrap_class = f'wrap img-{class_number}'
    proj_info_class = f'proj-info-{class_number}'
    section = template.format(wrap_class=wrap_class, proj_info_class=proj_info_class, num=i)
    sections.append(section)

html_content = '\n'.join(sections)

with open('generated_sections.html', 'w') as file:
    file.write(html_content)
