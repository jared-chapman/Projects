//hats (redeclare variables so effects from hats dont stay when switching hats
moveSpeed = 2;
jumpSpeed = 7;
grav = 0.2;
script_execute(scr_hats);



//get inputs
key_right = keyboard_check(ord('D'));
key_left = -keyboard_check(ord('A'));
key_jump = keyboard_check_pressed(vk_space);

//react to inputs
move = key_left + key_right;
hsp = move * moveSpeed;
if vsp < 10
    {
    vsp += grav; 
    }

if (place_meeting(x,y+1,obj_wall))
    {
    vsp = key_jump*-jumpSpeed;
    }

//horizontal collision
if (place_meeting(x+hsp,y,obj_wall))
    {
    while !place_meeting(x+sign(hsp),y,obj_wall)
        {
        x+=sign(hsp);
        }
    hsp = 0;    
    }

//vertical collision
if (place_meeting(x,y+vsp,obj_wall))
    {
    while !place_meeting(x,y+vsp,obj_wall)
        {
        y+=sign(vsp);
        }
    vsp = 0;    
    }
    
//calculate position        
x+=hsp;
y+=vsp;

//face Direction
if move != 0
    {
    image_xscale = sign(move);
    faceDir = sign(move);
    }
    
    
//portal
if place_meeting(x,y,obj_portal)
    {
    room_goto(1);
    }
