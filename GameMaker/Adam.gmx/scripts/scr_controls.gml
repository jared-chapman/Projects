rotateRight = keyboard_check(ord('D'));
rotateLeft  = keyboard_check(ord('A'));
throttle    = keyboard_check(ord('W'));
brake       = keyboard_check(ord('S'));
strafeR     = keyboard_check(ord('E'));
strafeL     = keyboard_check(ord('Q'));

rotate      = (rotateLeft-rotateRight)*rotateSpeed;



image_angle += rotate;
motion_add(image_angle, thrust*throttle);
motion_add(image_angle+90, strafeL*strafeSpeed);
motion_add(image_angle-90, strafeR*strafeSpeed);
if (brake){
    if (speed > brakeForce){
        speed -= brakeForce;
    }
}

