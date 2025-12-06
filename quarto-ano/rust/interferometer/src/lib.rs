pub mod quantum_matrix{

    pub mod states{
        
        pub const ZERO: [u8; 2] = [1, 0];
        pub const ONE: [u8; 2] = [0, 1];

    }

    pub mod operators{
        
        const HALF_AMPLITUDE : f32 = 0.70710678118;

        pub const UP_SPLITTER : [[f32; 2]; 2] = [[ -HALF_AMPLITUDE, HALF_AMPLITUDE ], [HALF_AMPLITUDE, HALF_AMPLITUDE]];
        pub const DOWN_SPLITTER : [[f32; 2]; 2] = [[ HALF_AMPLITUDE, HALF_AMPLITUDE ], [HALF_AMPLITUDE, -HALF_AMPLITUDE]];

    }

}
