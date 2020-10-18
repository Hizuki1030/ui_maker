import database_manage

a=database_manage.Database_manage(r"C:\Users\81909\Documents\python\ui_maker\動作確認用\databasetest\components_test.xml")
for sample in a.generate_code("m5stack"):
    print(sample)
