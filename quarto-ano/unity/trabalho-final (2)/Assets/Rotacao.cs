using UnityEngine;

public class PlanetRotation : MonoBehaviour
{
    public const float rotationSpeedMultiplier = 1000f;
    private const float earthRotation = 24f;
    private static float period = earthRotation * 3600f;
    private static float speed = 360f / period;
    private static float rotation = speed * rotationSpeedMultiplier;

    void Update()
    {
        transform.Rotate(Vector3.up, rotation * Time.deltaTime, Space.Self);
    }
}
