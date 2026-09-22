import re
content = open('resources/views/arena-belajar/live.blade.php', 'r', encoding='utf-8').read()
content = re.sub(r'const triggerRef = fb\.getRef\([^;]+;', 'const triggerRef = fb.getRef(`arena/{{ $session->id }}/sync_trigger`);', content)
open('resources/views/arena-belajar/live.blade.php', 'w', encoding='utf-8').write(content)
