#Working on an idea to track which tables at TX/RX Labs are and aren't available

#create a unique string name for each table, store other attributes about the 
#table in a dictionary with that name as the key
#would a table class be better?

tables = {'table0001': {'status': 'occupied', 'occupant': 'lab_member_256'}, 
    'table0002': {'status': 'occupied', 'occupant': 'lab_member_128'},
    'table0003': {'status': 'vacant', 'occupant': ''}
    }