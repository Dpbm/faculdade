using UnityEngine;

public class PlanetRotation : MonoBehaviour
{
    // Nome do planeta (para controle e depuração)
    public string planetName = "Terra";

    // Fator de escala para ajustar a rotação visivelmente no jogo
    [Tooltip("Multiplica a velocidade de rotação para fins visuais (ex: 1000 para acelerar).")]
    public float rotationSpeedMultiplier = 1000f;

    // Dicionário com o período de rotação em horas (rotação no próprio eixo)
    private readonly System.Collections.Generic.Dictionary<string, float> rotationPeriods = new System.Collections.Generic.Dictionary<string, float>()
    {
        { "Mercurio", 1407.6f },  // 58.6 dias
        { "Venus", -5832.5f },    // rotação retrógrada
        { "Terra", 24f },
        { "Marte", 24.6f },
        { "Jupiter", 9.9f },
        { "Saturno", 10.7f },
        { "Urano", -17.2f },      // retrógrada
        { "Netuno", 16.1f }
    };

    private float rotationSpeed; // graus por segundo

    void Start()
    {
        // Verifica se o planeta existe no dicionário
        if (!rotationPeriods.ContainsKey(planetName))
        {
            Debug.LogWarning($"[PlanetRotation] Planeta '{planetName}' não encontrado. Usando rotação da Terra como padrão.");
            planetName = "Terra";
        }

        // Calcula a velocidade de rotação (360° dividido pelo período em horas convertido para segundos)
        float period = rotationPeriods[planetName] * 3600f;
        rotationSpeed = 360f / period;
    }

    void Update()
    {
        // Aplica rotação contínua ao redor do eixo Y (ajuste se o eixo do planeta estiver diferente)
        transform.Rotate(Vector3.up, rotationSpeed * rotationSpeedMultiplier * Time.deltaTime, Space.Self);
    }
}
