if mouse_check_button_pressed(argument0) && !keyboard_check(vk_control){ //and canshoot
    if position==argument1{
     bullet = instance_create(x,y,argument2);
     with bullet{
            direction = other.image_angle
            image_angle = direction;
        }
    }
}
