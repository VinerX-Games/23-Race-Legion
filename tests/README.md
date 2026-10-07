Регрессионные тесты выполняют Lua 5.3 из исходных split-секций с моделью Warcraft natives.
Проверяются владельцы юнитов, AI-группы, телепорт при пустой армии, вложенные события
при выдаче приказов и отсутствие запуска моста по умолчанию.

```powershell
python -m pip install -r tests/requirements.txt
python -m unittest discover -s tests -v
```

Эти тесты не заменяют игровую проверку новой карты в Warcraft III.
