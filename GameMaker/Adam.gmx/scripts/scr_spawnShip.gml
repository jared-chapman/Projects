spawn = instance_create(room_width/2,room_height/2, obj_player);
with spawn{
    if argument0=="frigateOne"{
        script_execute(scr_frigateStats);
    }
}


