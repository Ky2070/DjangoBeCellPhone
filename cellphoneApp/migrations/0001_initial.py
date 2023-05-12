# Generated by Django 4.1.7 on 2023-03-19 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=20)),
                ('EstablishmentDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch_Product_Color',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField(default=0)),
                ('idBranch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Branch_Promotion_Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('discountRate', models.FloatField(default=0.0)),
                ('idBrandProductColor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.branch_product_color')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('names', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('names', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('deliveryAddress', models.CharField(max_length=50)),
                ('deliveryPhone', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=50)),
                ('nameManufacture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.manufacture')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('nameRole', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Earphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cellphoneApp.product')),
                ('connectionType', models.CharField(max_length=50)),
                ('Design', models.CharField(max_length=50)),
                ('Frequency_Response', models.CharField(max_length=50)),
            ],
            bases=('cellphoneApp.product',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cellphoneApp.product')),
                ('CPU', models.CharField(max_length=50)),
                ('RAM', models.CharField(max_length=50)),
                ('ROM', models.CharField(max_length=50)),
                ('Graphic_Card', models.CharField(max_length=50)),
                ('Battery', models.CharField(max_length=30)),
                ('operatorSystem', models.CharField(max_length=50)),
                ('Others', models.CharField(max_length=50)),
            ],
            bases=('cellphoneApp.product',),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cellphoneApp.product')),
                ('Operator_System', models.CharField(max_length=50)),
                ('CPU', models.CharField(max_length=50)),
                ('RAM', models.CharField(max_length=50)),
                ('ROM', models.CharField(max_length=50)),
                ('Battery', models.CharField(max_length=30)),
                ('Others', models.CharField(max_length=50)),
            ],
            bases=('cellphoneApp.product',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(blank=True, default='', max_length=100, null=True)),
                ('Gender', models.BooleanField(blank=True, default=False, null=True)),
                ('Hometown', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('userName', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('passWord', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('birthDay', models.DateField(auto_now=True, null=True)),
                ('phoneNumber', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('idRole', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.role')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.TextField()),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('timeStart', models.DateTimeField(auto_now=True)),
                ('timeEnd', models.DateTimeField(auto_now=True)),
                ('Active', models.BooleanField(default=False)),
                ('idBrandProductColor', models.ManyToManyField(through='cellphoneApp.Branch_Promotion_Product', to='cellphoneApp.branch_product_color')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Color',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.product')),
                ('nameColor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.color')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idBrandProductColor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.branch_product_color')),
                ('idOder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='idBranchProductColor',
            field=models.ManyToManyField(through='cellphoneApp.OrderDetail', to='cellphoneApp.branch_product_color'),
        ),
        migrations.AddField(
            model_name='order',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.user'),
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('linkImg', models.CharField(max_length=255)),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('contentComment', models.CharField(max_length=100)),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.product')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphoneApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='color',
            name='idProduct',
            field=models.ManyToManyField(through='cellphoneApp.Product_Color', to='cellphoneApp.product'),
        ),
        migrations.AddField(
            model_name='branch_promotion_product',
            name='idPromotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.promotion'),
        ),
        migrations.AddField(
            model_name='branch_product_color',
            name='idProductColor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cellphoneApp.product_color'),
        ),
        migrations.AddField(
            model_name='branch',
            name='idProductColors',
            field=models.ManyToManyField(through='cellphoneApp.Branch_Product_Color', to='cellphoneApp.product_color'),
        ),
    ]
