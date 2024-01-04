public abstract class Sample {
    protected String sampleID;
    protected String sampler;
    protected int date;
    protected String description;
    protected float X;
    protected float Y;
    protected float Z;
    
    public Sample(String sampleID, String sampler, int date, float X, float Y, float Z){
        this.setSample(sampleID);
        this.setSampler(sampler);
        this.setint(date);
        this.setX(X);
        this.setY(Y);
        this.setZ(Z);
    }

    public Sample(String sampleID, String sampler, int date, float X, float Y, float Z, String description){
        this.setSample(sampleID);
        this.setSampler(sampler);
        this.setint(date);
        this.setX(X);
        this.setY(Y);
        this.setZ(Z);
        this.setDesc(description);
    }


    public String getSampleID(){
        return (this.sampleID);
    }

    public String getSampler(){
        return (this.sampler);
    }

    public float[] getCord(){
        float[] coordinates = new float[3];
        coordinates[0] = this.X;
        coordinates[1] = this.Y;
        coordinates[2] = this.Z;
        return coordinates;
    }

    public String setSample(String sampleID){
        return (sampleID);
    }

    public String setSampler(String sampler){
        return (sampler);
    }

    public String setDesc(String description){
        return (description);
    }
    
    //this setter for date will need to be updated to fill from phone's calendar

    public int setint(int day){
        return (day);
    }

    //these XYZ setters need updated to pull from an android GPS

    public float setX(float X){
        return (X);
    }

    public float setY(float Y){
        return (Y);
    }

    public float setZ(float Z){
        return (Z);
    }



}
