using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Car : MonoBehaviour
{

    public float vel;
    private bool firstPerson = false;
    
    
    private List<Camera> cameras = new List<Camera>();
    private List<GameObject> wheels = new List<GameObject>();


    private static Vector3 initialPositon = Vector3.zero;
    private static Quaternion initialRotation = Quaternion.identity;

    void Start()
    {

        cameras.Add(GameObject.Find("Main Camera").GetComponent<Camera>());
        cameras.Add(GameObject.Find("fp-camera").GetComponent<Camera>());

        for(int i = 1; i <= 4; i++){
            wheels.Add(GameObject.Find($"wheel{i}"));
        }

        switchCamera();
    }

    private bool nextCamera(){
        return !firstPerson;
    }

    private void switchCamera(){
        cameras[0].gameObject.SetActive(!firstPerson);
        cameras[1].gameObject.SetActive(firstPerson);
    }

    private void reset(){
        transform.position = initialPositon;
        transform.localRotation = initialRotation;
        firstPerson = false;
        switchCamera();
    }

    private void RotateWheels(int dir){
        float rot = dir * 90 * vel * Time.deltaTime;
        foreach (GameObject wheel in wheels){
            wheel.transform.Rotate(0, 0, rot);
        }
    }

    void Update()
    {

        float inc = vel*Time.deltaTime;
        float rot = 30*vel*Time.deltaTime;
        if(Input.GetKeyDown(KeyCode.W)){
            transform.Translate(inc,0,0);
            RotateWheels(-1);
        }else if(Input.GetKeyDown(KeyCode.S)){
            transform.Translate(-inc,0,0);
            RotateWheels(1);
        }else if(Input.GetKeyDown(KeyCode.A)){
            transform.Rotate(0,-rot,0);  
            RotateWheels(1);
        }else if(Input.GetKeyDown(KeyCode.D)){
            transform.Rotate(0,rot,0);  
            RotateWheels(1);
        }
        
        if(Input.GetKeyDown(KeyCode.C)){
            firstPerson = !firstPerson;
            switchCamera();
        }

        if(Input.GetKeyDown(KeyCode.R)){
            reset();
        }
    }
}
