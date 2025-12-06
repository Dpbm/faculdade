using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shoot : MonoBehaviour
{

    public Rigidbody bullet;
    private float velocidade = 1300f;

    void Start()
    {
        
    }

    void Update()
    {
        if(Input.GetButtonDown("Fire1")) {
            Rigidbody instance = (Rigidbody)Instantiate(bullet,transform.position,transform.rotation);
            Vector3 forward = transform.TransformDirection(Vector3.forward);
            instance.AddForce(forward*velocidade);

            Destroy(instance.gameObject,2.5f);
        }
    }
}
