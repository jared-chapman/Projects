//This is a temporary script to manage scrolling through weapons
//Eventually this will be replaced with an inventory/equip system

if keyboard_check(vk_control) && mouse_check_button_pressed(mb_left) && position == "left"{
    switch(state){
        case state_empty:
            state_switch("Cannon");
            break;
        case state_cannon:
            state_switch("GravBomb");
            break;
        case state_gravBomb:
            state_switch("MiningLaser");
            break;
        case state_miningLaser:
            state_switch("Empty")
            break;
    }   
}

if keyboard_check(vk_control) && mouse_check_button_pressed(mb_right) && position == "right"{
    switch(state){
        case state_empty:
            state_switch("Cannon");
            break;
        case state_cannon:
            state_switch("GravBomb");
            break;
        case state_gravBomb:
            state_switch("MiningLaser");
            break;
        case state_miningLaser:
            state_switch("Empty")
            break;
    }   
}

