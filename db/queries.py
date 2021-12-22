check_registered_id_query = '''
SELECT * FROM alliance.registered_id
where phone = :id
'''


insert_user_query = '''
INSERT INTO `alliance`.`user_main`
(`phone`,
`context_id`)
VALUES
(:msg,
:text_id)
'''


Check_user_query = '''
SELECT * FROM alliance.user_main
where context_id = :text_id
'''


check_total_acc_query = '''
SELECT * from alliance.registered_id
where phone = (select phone from alliance.user_main where context_id = :text_id)
'''

INSERT_query = '''
INSERT INTO `alliance`.`complain_support`
(`context_id`,
`registered_id`,
`description`,
`complain`)
VALUES
(:context_id,
:registered_id,
:description,
:complain);
'''


open_complain_query = '''
SELECT * FROM alliance.complain_support where registered_id = :registered_id
'''
