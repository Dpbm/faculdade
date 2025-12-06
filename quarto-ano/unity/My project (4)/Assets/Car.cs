using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{

    public float vel;

    void Start()
    {
        

    }

    void RotateWheels(int dir){
        float rot = dir * 90 * vel * Time.deltaTime;
        transform.Find("wheel1").Rotate(0, 0, rot);
        transform.Find("wheel2").Rotate(0, 0, rot);
        transform.Find("wheel3").Rotate(0, 0, rot);
        transform.Find("wheel4").Rotate(0, 0, rot);
    }

    void Update()
    {

        float inc = vel*Time.deltaTime;
        if(Input.GetKeyDown(KeyCode.W)){
            transform.Translate(inc,0,0);
            RotateWheels(-1);
        }else if(Input.GetKeyDown(KeyCode.S)){
            transform.Translate(-inc,0,0);
            RotateWheels(1);
        }

    }
}
