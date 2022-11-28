from django.db import models


class AttackElementCorrectParam(models.Model):
    Row_ID = models.IntegerField()

    Physical_Scaling_STR = models.BooleanField()
    Physical_Scaling_DEX = models.BooleanField()
    Physical_Scaling_INT = models.BooleanField()
    Physical_Scaling_FAI = models.BooleanField()
    Physical_Scaling_ARC = models.BooleanField()

    Magic_Scaling_STR = models.BooleanField()
    Magic_Scaling_DEX = models.BooleanField()
    Magic_Scaling_INT = models.BooleanField()
    Magic_Scaling_FAI = models.BooleanField()
    Magic_Scaling_ARC = models.BooleanField()

    Fire_Scaling_STR = models.BooleanField()
    Fire_Scaling_DEX = models.BooleanField()
    Fire_Scaling_INT = models.BooleanField()
    Fire_Scaling_FAI = models.BooleanField()
    Fire_Scaling_ARC = models.BooleanField()

    Lightning_Scaling_STR = models.BooleanField()
    Lightning_Scaling_DEX = models.BooleanField()
    Lightning_Scaling_INT = models.BooleanField()
    Lightning_Scaling_FAI = models.BooleanField()
    Lightning_Scaling_ARC = models.BooleanField()

    Holy_Scaling_STR = models.BooleanField()
    Holy_Scaling_DEX = models.BooleanField()
    Holy_Scaling_INT = models.BooleanField()
    Holy_Scaling_FAI = models.BooleanField()
    Holy_Scaling_ARC = models.BooleanField()


class CalcCorrectGraph(models.Model):
    used_for = models.CharField(max_length=255)

    stat_0 = models.FloatField()
    stat_1 = models.FloatField()
    stat_2 = models.FloatField()
    stat_3 = models.FloatField()
    stat_4 = models.FloatField()

    grow_0 = models.FloatField()
    grow_1 = models.FloatField()
    grow_2 = models.FloatField()
    grow_3 = models.FloatField()
    grow_4 = models.FloatField()

    exponent_0 = models.FloatField()
    exponent_1 = models.FloatField()
    exponent_2 = models.FloatField()
    exponent_3 = models.FloatField()
    exponent_4 = models.FloatField()


class CalcCorrectGraphID(models.Model):

    Model_ID = models.IntegerField()
    name = models.CharField(max_length=255)

    CalcCorrectGraph_ID_Physical = models.IntegerField()
    CalcCorrectGraph_ID_Magic = models.IntegerField()
    CalcCorrectGraph_ID_Fire = models.IntegerField()
    CalcCorrectGraph_ID_Lightning = models.IntegerField()
    CalcCorrectGraph_ID_Holy = models.IntegerField()


class RawData(models.Model):

    Model_ID = models.IntegerField()
    Name = models.CharField(max_length=255)
    Reinforce_Type_ID = models.IntegerField()

    Physical_Attack = models.IntegerField()
    Magic_Attack = models.IntegerField()
    Fire_Attack = models.IntegerField()
    Lightning_Attack = models.IntegerField()
    Holy_Attack = models.IntegerField()
    Stamina_Attack = models.IntegerField()

    STR_scaling = models.IntegerField()
    DEX_scaling = models.IntegerField()
    INT_scaling = models.IntegerField()
    FAI_scaling = models.IntegerField()
    ARC_scaling = models.IntegerField()

    Physical_Guard = models.IntegerField()
    Magic_Guard = models.IntegerField()
    Fire_Guard = models.IntegerField()
    Lightning_Guard = models.IntegerField()
    Holy_Guard = models.IntegerField()
    Guard_boost = models.IntegerField()
    Resistance_Guard = models.IntegerField()

    Upgrade_price = models.IntegerField()

    Effect_1 = models.IntegerField()
    Effect_1_Type = models.CharField(max_length=255)
    Effect_2 = models.IntegerField()
    Effect_2_Type = models.CharField(max_length=255)
    Attack_Element_Correct_ID = models.IntegerField()

    Infusable = models.CharField(max_length=255)
    Max_Upgrade = models.IntegerField()
    Required_Str = models.IntegerField()
    Required_Dex = models.IntegerField()
    Required_Int = models.IntegerField()
    Required_Fai = models.IntegerField()
    Required_Arc = models.IntegerField()

    Weapon_Type = models.CharField(max_length=255)
    Physical_Damage_Type = models.CharField(max_length=255)
    Weight = models.FloatField()
    Attack_Power_Crit = models.IntegerField()
    TwoH_STR_Bonus = models.CharField(max_length=255)
    Sort_Group_Type = models.IntegerField()
    Sort_Group_ID = models.IntegerField()
    Sort_ID = models.IntegerField()

    def __str__(self):
        return self.Name


class ReinforceParamWeapon(models.Model):

    Model_ID = models.IntegerField()

    Physical_Attack = models.FloatField()
    Magic_Attack = models.FloatField()
    Fire_Attack = models.FloatField()
    Lightning_Attack = models.FloatField()
    Holy_Attack = models.FloatField()
    Stamina_Attack = models.FloatField()

    Str_Scaling = models.FloatField()
    Dex_Scaling = models.FloatField()
    Int_Scaling = models.FloatField()
    Fai_Scaling = models.FloatField()
    Arc_Scaling = models.FloatField()

    Physical_Guard = models.FloatField()
    Magic_Guard = models.FloatField()
    Fire_Guard = models.FloatField()
    Lightning_Guard = models.FloatField()
    Holy_Guard = models.FloatField()
    Stability_Guard = models.FloatField()
    Resistance_Guard = models.FloatField()

    Upgrade_Price = models.FloatField()

    Effect_1_Offset = models.IntegerField()
    Effect_2_Offset = models.IntegerField()