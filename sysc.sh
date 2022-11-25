flag=$1
if [ "$flag" != "--cli" ]
then
    clear
    echo "UI App"
    python3 ui_app.py
else
    clear
    echo "CLI App"
    python3 cli_app.py
fi
# python3 ui_app.py