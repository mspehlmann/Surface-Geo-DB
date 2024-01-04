import javax.lang.model.type.NullType;

public class Sediment extends Sample{
    private int meshSize1;
    private int meshSize2;
    private String energy;
    private float streamPh;

    // using overloaded constructors so that seds can also be taken from dry areas
    Sediment(String sampleID, String sampler, int date, float X, 
        float Y, float Z, String color, String description, 
        int meshSize1, int meshSize2, String energy, float streamPh){
            super(sampleID, sampler, date, X, Y, Z, description);
            this.setMesh1(meshSize1);
            this.setMesh2(meshSize2);
            this.setEnergy(energy);
            this.setPh(streamPh);
        }

    Sediment(String sampleID, String sampler, int date, float X, 
        float Y, float Z, String color, int meshSize1, int meshSize2, 
        String energy, float streamPh){
            super(sampleID, sampler, date, X, Y, Z);
            this.setMesh1(meshSize1);
            this.setMesh2(meshSize2);
            this.setEnergy(energy);
            this.setPh(streamPh);
        }

    Sediment(String sampleID, String sampler, int date, float X, 
        float Y, float Z, String color, String description, 
        int meshSize1, int meshSize2){
            super(sampleID, sampler, date, X, Y, Z, description);
            this.setMesh1(meshSize1);
            this.setMesh2(meshSize2);
        }
    
    Sediment(String sampleID, String sampler, int date, float X, 
        float Y, float Z, int meshSize1, int meshSize2){
            super(sampleID, sampler, date, X, Y, Z);
            this.setMesh1(meshSize1);
            this.setMesh2(meshSize2);
        }

    // probably should just make these return a list of meshes
    public int getMeshes1(){
        return (this.meshSize1);
    }
    public int getMeshes2(){
        return (this.meshSize2);
    }

    public String getEnergy(){
        return (this.energy);
    }

    public float getStreamPh(){
        return (this.streamPh);
    }

    public int setMesh1(int meshSize1){
        return (meshSize1);
    }

    public int setMesh2(int meshSize2){
        return (meshSize2);
    }

    public String setEnergy(String streamEnergy){
        return (streamEnergy);
    }

    public float setPh(float ph){
        return (ph);
    }
}
