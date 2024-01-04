public class Soil extends Sample{
    
    private String color;
    private float depth;
    
    public Soil(String sampleID, String sampler, int date, float X, 
            float Y, float Z, String color, float depth){
        super(sampleID, sampler, date, X, Y, Z);
        this.setColor(color);
        this.setDepth(depth);
    }

    public Soil(String sampleID, String sampler, int date, float X, 
            float Y, float Z, String color, float depth, String description){
        super(sampleID, sampler, date, X, Y, Z, description);
        this.setColor(color);
        this.setDepth(depth);
    }

    public String getColor(){
        return (this.color);
    }

    public float getDepth(){
        return (this.depth);
    }

    public String setColor(String colorOfDirt){
        return (colorOfDirt);
    }

    public float setDepth(float depthOfDirt){
        return (depthOfDirt);
    }
}
