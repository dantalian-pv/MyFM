My File Manager
========================================================================

# Description
MyFM_PFT_win2 - it is a File Manager with minimum functionality.
The main feature is a fast navigation over text, photo and video files.

# Software requirements
To run the application `python3` is required.
To install required dependencies run the next command:
for Debian, Ubuntu:
`sudo apt install python3-tk python3-magic python3-pil python3-pil.imagetk`

for OpenSuse:
`sudo zypper in python3-tk python3-magic python3-Pillow python3-Pillow-tk`

# Running application
To run the application 
1. Download `MyFM_PFT_win2.py` from GitHub repository
2. Go into the folder where the file was downloaded
3. Execute the next command in a console: 
`$> python3 MyFM_PFT_win2.py`

# Usage
After the application was started, expand appeared window to a full screen.

## Files list view
- Names of text, photo and video files have different colored background, all other files have white background
- The name of selected file is shown in the bottom, if it is a line, a full real path will be shown as well.

## Navigation with mouse
1. Right panel is shown in a full screen mode shows text, image, video files previews
2. Double cline on a top address panel - opens dialog to choose a new path
3. Double click on ". . ." - goes to parent folder
4. Double click on a folder name - goes to selected folder
5. Double click on a file - opens file in a default application
6. Single click on a text, image or video file - shows preview on a right panel
7. Right click on any area - show context menu with:
    - Show/Hide hidden files and folders
    - Delete file/folder

## Sorting files
1. Single click on a column name - sort files by it property
2. For reverse sorting click on the column name again

### Sorting features
1. Column 'Ext' - sort folders by an amount of children folders
2. Column 'Size' - sort folders by an amount of total children elements in it

## Keyboard navigation
1. "Up" and "Down" arrows to navigate over files/folders list in a left panel
2. "Escape" - close context menu or "Help" window
3. "Space" - open file in a default application (no action with links)
4. "Ctrl+H" - show/hide hidden files

========================================================================

Описание:
MyFM_PFT_win2 - это файловый менеджер с минимальными возможностями.
Предназначен для быстрой навигации по списку текстовых, фото и видео файлов.
После старта программы, двойным кликом по шапке окна, разверните MyFM_PFT_win2 на весь экран.

Особенности списка файлов:
имена текстовых, фото и медиа файлов выделяются цветным фоном,
все остальные файлы - белым фоном.
Имя выбранного файла дублируется в нижнем строке окна ФМ.
Если это ссылка, то указывается полный путь ссылки и полный реальный путь.

Основное управление кнопками мыши:
1. Двойной клик по имени окна  "Файловый менеджер":
    ФМ развернется на весь экран и откроется окно справа,
    для просмотра содержимого текстовых файлов
2. Двойной клик по строке адреса папки:
    откроется меню выбора новой папки для работы
3. Двойной клик по имени ". . ."
    переход в папку родителя
4. Двойной клик по имени папки:
    переход в эту папку
5. Двойной клик по имени файла, файл запустится приложением по умолчанию
6. Одинарный клик по имени текстового файла или image (только в полноэкранном режиме):
    просмотр содержимого файла
    (по списку файлов можно передвигаться при помощи клавиш курсора вверх и вниз)
7. Клик Правой кнопкой мыши в любом месте ФМ вызовет меню:
    для Показать/Скрыть имена файлов начинающихся с точки (скрытые файлы)
    для Удаления файла

Сортировка файлов:
1. Одинарный клик по имени столбца:
    файлы сортируются в соответствии с именем этого столбца
2. Повторный клик по имени того же столбца:
    обратная сортировка в соответствии с именем этого столбца

Особенности сортировки:
1. Столбец 'Ext':
    папки сортируются по количеству вложенных папок
2. Столбец 'Size':
    папки сортируются по количеству элементов в папке

Управление клавишами клавиатуры:
1. стрелками курсора "вверх" и "вниз" - передвижение по списку файлов
2. "Escape" - закрыть меню и окно "Help"
3. "Пробел" - файл запустится приложением по умолчанию.
    Переход по ссылке запрещен, поэтому нет действий при нажатии на пробел
4. "Ctrl+H" показать/скрыть скрытые файлы
