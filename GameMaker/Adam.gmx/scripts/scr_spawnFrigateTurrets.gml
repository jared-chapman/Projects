rightGun = instance_create(x,y,obj_turret)
with rightGun{
    position = "right";
    len = other.rightWingLen;
    dir = other.rightWingDir;
}

leftGun = instance_create(x,y,obj_turret)
with leftGun{
    position = "left";
    len = obj_player.leftWingLen;
    dir = obj_player.leftWingDir;
}
