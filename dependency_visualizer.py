#!/usr/bin/env python3
import argparse
import sys
import os

class DependencyVisualizer:
    def __init__(self):
        self.params = {}
    
    def parse_arguments(self):
        """Парсинг аргументов командной строки"""
        parser = argparse.ArgumentParser(
            description='Визуализатор графа зависимостей для Maven пакетов',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
Примеры использования:
  python dependency_visualizer.py -p "com.example:my-app" -v "1.0.0"
  python dependency_visualizer.py --package "org.springframework:spring-core" --version "5.3.0" --output "dependencies.png"
            '''
        )
        
        # Обязательные параметры
        parser.add_argument(
            '-p', '--package',
            required=True,
            help='Имя анализируемого пакета (формат: groupId:artifactId)'
        )
        
        parser.add_argument(
            '-v', '--version',
            required=True,
            help='Версия пакета'
        )
        
        # Опциональные параметры
        parser.add_argument(
            '-u', '--url',
            default='https://repo1.maven.org/maven2/',
            help='URL Maven репозитория (по умолчанию: центральный Maven репозиторий)'
        )
        
        parser.add_argument(
            '-t', '--test-mode',
            action='store_true',
            help='Режим работы с тестовым репозиторием'
        )
        
        parser.add_argument(
            '-f', '--file',
            help='Путь к файлу тестового репозитория (используется в тестовом режиме)'
        )
        
        parser.add_argument(
            '-o', '--output',
            default='dependency_graph.png',
            help='Имя сгенерированного файла с изображением графа'
        )
        
        return parser.parse_args()
    
    def validate_arguments(self, args):
        """Валидация аргументов"""
        errors = []
        
        # Проверка формата имени пакета
        if ':' not in args.package:
            errors.append("Имя пакета должно быть в формате groupId:artifactId")
        
        # Проверка версии
        if not args.version or args.version.isspace():
            errors.append("Версия пакета не может быть пустой")
        
        # Проверка тестового режима
        if args.test_mode and not args.file:
            errors.append("В тестовом режиме должен быть указан путь к файлу")
        
        if not args.test_mode and args.file:
            errors.append("Файл тестового репозитория можно указать только в тестовом режиме")
        
        # Проверка выходного файла
        if not args.output:
            errors.append("Имя выходного файла не может быть пустым")
        elif not args.output.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
            errors.append("Выходной файл должен иметь расширение изображения (.png, .jpg, .jpeg, .svg)")
        
        return errors
    
    def print_parameters(self, args):
        """Вывод всех параметров в формате ключ-значение"""
        print("=== Параметры конфигурации ===")
        print(f"Имя пакета: {args.package}")
        print(f"Версия пакета: {args.version}")
        print(f"URL репозитория: {args.url}")
        print(f"Режим тестирования: {'Включен' if args.test_mode else 'Выключен'}")
        
        if args.test_mode and args.file:
            print(f"Файл тестового репозитория: {args.file}")
        
        print(f"Выходной файл: {args.output}")
        print("=" * 32)
    
    def run(self):
        """Основной метод запуска"""
        try:
            # Парсинг аргументов
            args = self.parse_arguments()
            
            # Валидация
            errors = self.validate_arguments(args)
            if errors:
                print("Ошибки валидации:")
                for error in errors:
                    print(f"  - {error}")
                sys.exit(1)
            
            # Вывод параметров (требование этапа 1)
            self.print_parameters(args)
            
            # Здесь будет основная логика в следующих этапах
            print("✓ Конфигурация успешно загружена!")
            print("✓ Готово к сбору данных о зависимостях...")
            
        except argparse.ArgumentError as e:
            print(f"Ошибка в аргументах: {e}")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            sys.exit(1)
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            sys.exit(1)

def main():
    visualizer = DependencyVisualizer()
    visualizer.run()

if __name__ == '__main__':
    main()
